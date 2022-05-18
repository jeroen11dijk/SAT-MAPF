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
    # print(mMstar(problem))
    print(SATColored(problem))
    print(SATColoredCNF(problem))
    print(MaxSATColored(problem))
