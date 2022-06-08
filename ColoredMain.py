import itertools
import sys

from MAXSATSolverColored import SATSolverColored
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


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


if __name__ == "__main__":
    graph = sys.argv[1]
    scen = sys.argv[2]
    algorithm = sys.argv[3]
    problem = BaseProblem(graph, scen)
    if len(open(str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()) > 1:
        prev_agents = int(open(str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()[-2].split("a")[0])
    else:
        prev_agents = int(scen.split("/")[1].split("a")[0])
    if prev_agents == int(scen.split("/")[1].split("a")[0]) or prev_agents == int(scen.split("/")[1].split("a")[0]) - 1:
        file = open(str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt', 'a')
        if int(algorithm) == 1:
            res, cost = SATSolverColored(problem).solve_cnf()
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 2:
            res, cost = SATSolverColored(problem).solve_cnf(True)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 3:
            res, cost = SATSolverColored(problem, inflation=1.25).solve_cnf(True)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 4:
            res, cost = mMstar(problem)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
    else:
        print("skip")

