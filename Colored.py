import itertools

from SATSolverColored import SATSolverColored
from main import timeout
from mstar import Mstar
from problem_classes import BaseProblem, MAPFW
from utils import convert_grid_dict_ints, dijkstra_distance


@timeout(60.0)
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
        problems.append(new_problem)
        new_problem.get_heuristic(distances)
    problems.sort(key=lambda x: x.heuristic)
    res = float("inf")
    opt_path = None
    for i, problem in enumerate(problems):
        if problem.heuristic > res:
            break
        path, cost = Mstar(problem.graph, tuple(problem.starts), ((), (), (), (), (), ()),
                           tuple(problem.goals), tsp_cache).solve()
        if cost < res:
            res = cost
            opt_path = path
    return opt_path, res

@timeout(60.0)
def MaxSATColored(problem):
    return SATSolverColored(problem).solve(True)

@timeout(60.0)
def SATColored(problem):
    return SATSolverColored(problem).solve(False)

@timeout(60.0)
def SATColoredCNF(problem):
    return SATSolverColored(problem).solve_cnf()

if __name__ == '__main__':
    problem = BaseProblem("graph.graph", "problem.scen")
    print(problem.starts)
    print(problem.goals)
    # problem.graph = {0: [4], 2: [6, 3], 3: [2, 7], 4: [0, 8, 5], 5: [4, 9, 6], 6: [2, 5, 10, 7], 7: [3, 6, 11], 8: [4, 12, 9], 9: [5, 8, 13, 10], 10: [6, 9, 14, 11], 11: [7, 10, 15], 12: [8, 13], 13: [9, 12, 14], 14: [10, 13, 15], 15: [11, 14]}
    # problem.starts = [[4, 3]]
    # problem.goals = [[15, 11]]
    # problem.n_agents = 2
    for vertex in problem.graph:
        problem.distances[vertex] = dijkstra_distance(problem.graph, vertex)
    print(SATColored(problem))
    print(SATColoredCNF(problem))
