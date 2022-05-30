import itertools
import os

from MAXSATSolverColored import SATSolverColored
from main import timeout
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


@timeout(300.0)
def mMstar(problem):
    matches = []
    for team in range(len(problem.starts)):
        a = problem.starts[team]
        b = problem.goals[team]
        combinations = [list(zip(comb, b)) for comb in list(itertools.permutations(a, len(b)))]
        matches.append(combinations)
    problems = []
    distances = {}
    tsp_cache = {}
    for match in list(itertools.product(*matches)):
        new_problem = MAPFW()
        new_problem.update(problem, match)
        try:
            new_problem.get_heuristic(distances)
            problems.append(new_problem)
        except:
            pass
    problems.sort(key=lambda x: x.heuristic)
    res = float("inf")
    opt_path = None
    for i, problem in enumerate(problems):
        if problem.heuristic > res:
            break
        waypoints = ((),) * problem.n_agents
        path, cost = Mstar(problem.graph, tuple(problem.starts), waypoints,
                           tuple(problem.goals), tsp_cache).solve()
        if cost < res:
            res = cost
            opt_path = path
    return opt_path, res


@timeout(300.0)
def MaxSATColored(problem):
    return SATSolverColored(problem).solve(True)


@timeout(300.0)
def MaxSATColoredInflated(problem):
    return SATSolverColored(problem, inflation=1.25).solve(True)


@timeout(300.0)
def SATColoredCNF(problem):
    return SATSolverColored(problem).solve_cnf()


if __name__ == '__main__':
    res = {"MaxSATColored": 0, "MaxSATColoredInflated": 0, "mMstar": 0, "SATColoredCNF": 0}
    file = ""
    done = set()
    ten = 0
    extra = []
    extra_inflated = []
    graph = 'grid_random_3t_64n_8b_8g_10.0r.graph'
    for scene in sorted(os.listdir('grid_random_3t_64n_8b_8g_10.0r/'), key=lambda x: int(x.split('_')[7][0:-1])):
        main_problem = BaseProblem(graph, 'grid_random_3t_64n_8b_8g_10.0r/' + scene)
        ten += 1
        costs = {"MaxSATColored": -1, "MaxSATColoredInflated": -1, "mMstar": -1, "SATColoredCNF": -1}
        solvers = [MaxSATColored, MaxSATColoredInflated, mMstar, SATColoredCNF]
        for func in solvers:
            if func.__name__ not in done:
                try:
                    costs[func.__name__] = func(main_problem)[1]
                    res[func.__name__] += 1
                except:
                    pass
        if costs["MaxSATColored"] > costs["SATColoredCNF"]:
            extra.append(((costs["MaxSATColored"] - costs["SATColoredCNF"]) / costs["SATColoredCNF"])*100)
        if costs["MaxSATColoredInflated"] > costs["SATColoredCNF"]:
            extra_inflated.append(((costs["MaxSATColoredInflated"] - costs["SATColoredCNF"]) / costs["SATColoredCNF"])*100)
        if ten == 10:
            file += str(scene.split('_')[7][0:-1]) + ": " + str(res) + '\n'
            for key in res.keys():
                if res[key] == 0:
                    done.add(key)
            res = {"MaxSATColored": 0, "MaxSATColoredInflated": 0, "mMstar": 0, "SATColoredCNF": 0}
            ten = 0
    file += str(extra) + "\n"
    file += str(extra_inflated)
    open("results.txt", "w").write(file)
