import itertools
import sys

from MAXSATSolver import SATSolver
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


def pmSAT(problem, maxsat=False):
    matches = []
    for team in range(len(problem.starts)):
        a = problem.starts[team]
        b = problem.goals[team]
        combinations = [list(zip(comb, b)) for comb in list(itertools.permutations(a, len(b)))]
        matches.append(combinations)
    problems = []
    for match in list(itertools.product(*matches)):
        new_problem = BaseProblem()
        new_problem.graph = problem.graph
        new_problem.n_agents = problem.n_agents
        new_problem.distances = problem.distances
        new_problem.waypoints = problem.waypoints
        for team in match:
            for agent in team:
                new_problem.starts.append(agent[0])
                new_problem.goals.append(agent[1])
        for i in range(new_problem.n_agents):
            current = new_problem.starts[i]
            goal = new_problem.goals[i]
            new_problem.heuristics.append(new_problem.distances[goal][current])
        problems.append(new_problem)
    problems.sort(key=lambda x: sum(x.heuristics))
    res = float("inf")
    opt_path = None
    for i, problem in enumerate(problems):
        if sum(problem.heuristics) > res:
            break
        path, cost = SATSolver(problem).solve_cnf(maxsat)
        if cost < res:
            res = cost
            opt_path = path
    return opt_path, res


if __name__ == "__main__":
    graph = sys.argv[1]
    scen = sys.argv[2]
    algorithm = sys.argv[3]
    problem = BaseProblem(graph, scen)
    if len(open("colored_results/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()) > 1:
        prev_agents = int(
            open("colored_results/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()[-2].split(
                "a")[0])
        prev_suffix = int(
            open("colored_results/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()[-2].split(
                "_")[1].split(".")[0])
    else:
        prev_agents = int(scen.split("/")[1].split("a")[0])
        prev_suffix = int(scen.split("/")[1].split("_")[1].split(".")[0]) - 1
    curr_agents = int(scen.split("/")[1].split("a")[0])
    curr_suffix = int(scen.split("/")[1].split("_")[1].split(".")[0])
    same_agents = curr_agents == prev_agents and curr_suffix > prev_suffix
    more_agents = curr_agents - 1 == prev_agents
    if same_agents or more_agents:
        file = open("colored_results/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt', 'a')
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
        elif int(algorithm) == 5:
            res, cost = pmSAT(problem)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 6:
            res, cost = pmSAT(problem, True)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
    else:
        print("skip")
