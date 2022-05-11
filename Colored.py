import itertools

from MAXSATSolverColored import MAXSATSolverColored
from mstar import Mstar
from problem_classes import BaseProblem, MAPFW

if __name__ == '__main__':
    problem = BaseProblem(1, 2, 4, 0.1)
    print(problem.graph)
    print(problem.starts)
    print(problem.goals)
    res, cost = MAXSATSolverColored(problem).solve()
    print(res, cost)
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
        new_problem.get_heuristic(distances, tsp_cache)
    problems.sort(key=lambda x: x.heuristic)
    res = float("inf")
    opt_path = None
    for i, problem in enumerate(problems):
        print(problem.heuristic)
        if problem.heuristic > res:
            break
        path, cost = Mstar(problem.graph, tuple(problem.starts), ((), (), (), ()),
                        tuple(problem.goals), tsp_cache).solve()
        if cost < res:
            res = cost
            opt_path = path
    print(opt_path, res)
