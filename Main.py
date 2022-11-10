import itertools

from ColoredMain import mMstar
from MAXSATSolver import SATSolver
from MAXSATSolverColored import SATSolverColored
from MAXSATSolverCombined import SATSolverCombined
from MAXSATSolverWaypoints import SATSolverWaypoints
from problem_classes import BaseProblem
from utils import dijkstra_distance


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


if __name__ == '__main__':
        problem = BaseProblem("grid8.graph", "grid8/4a_3.scen")
        b = SATSolverColored(problem).solve_cnf(False)
        print(b)

