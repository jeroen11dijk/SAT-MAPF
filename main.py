import functools
import multiprocessing.pool
import random

from MAXSATSolver import MAXSATSolver
from MAXSATSolverUpper import MAXSATSolverUpper
from StandardSolver import StandardSolver
from WMStar.mstar import Mstar
from problem_classes import BaseProblem
from utils import dijkstra_distance


def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""

    def timeout_decorator(item):
        """Wrap the original function."""

        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)

        return func_wrapper

    return timeout_decorator


@timeout(60.0)
def solver0(problem):
    return StandardSolver(problem).solve()


@timeout(10.0)
def solver1(problem):
    return MAXSATSolver(problem).solve()


@timeout(60.0)
def solver2(problem):
    return MAXSATSolverUpper(problem).solve()


@timeout(10.0)
def solver3(problem):
    return Mstar(problem.graph, tuple(problem.starts), ((), (), (), (), (), (), (), (), (), ()),
                 tuple(problem.goals), {}).solve()


if __name__ == '__main__':
    # for file in os.listdir('carrousel_random_25n_5b_5g_0.0r'):
    #     main_problem = BaseProblem('carrousel_random_25n_5b_5g_0.0r.graph', 'carrousel_random_25n_5b_5g_0.0r/' + file)
    #     ten += 1
    #     print(file)
    #     for i, func in enumerate([solver3]):
    #         try:
    #             func(main_problem)
    #             res += 1
    #         except:
    #             pass
    #     if ten == 10:
    #         print(res)
    #         res = 0
    #         ten = 0
    problem = BaseProblem()
    problem.graph = {0: [8], 2: [10, 3], 3: [2, 11], 5: [13, 6], 6: [5, 14, 7], 7: [6], 8: [0, 16], 10: [2, 18, 11], 11: [3, 10, 12], 12: [11, 20, 13], 13: [5, 12, 21, 14], 14: [6, 13, 22], 16: [8, 24, 17], 17: [16, 25, 18], 18: [10, 17, 26], 20: [12, 28, 21], 21: [13, 20, 29, 22], 22: [14, 21, 30, 23], 23: [22, 31], 24: [16, 32, 25], 25: [17, 24, 33, 26], 26: [18, 25, 34, 27], 27: [26, 35, 28], 28: [20, 27, 36, 29], 29: [21, 28, 37, 30], 30: [22, 29, 38, 31], 31: [23, 30, 39], 32: [24, 40, 33], 33: [25, 32, 41, 34], 34: [26, 33, 42, 35], 35: [27, 34, 43, 36], 36: [28, 35, 44, 37], 37: [29, 36, 45, 38], 38: [30, 37, 46, 39], 39: [31, 38, 47], 40: [32, 48, 41], 41: [33, 40, 49, 42], 42: [34, 41, 50, 43], 43: [35, 42, 44], 44: [36, 43, 52, 45], 45: [37, 44, 53, 46], 46: [38, 45, 54, 47], 47: [39, 46, 55], 48: [40, 56, 49], 49: [41, 48, 57, 50], 50: [42, 49, 58], 52: [44, 60, 53], 53: [45, 52, 61, 54], 54: [46, 53, 62, 55], 55: [47, 54, 63], 56: [48, 57], 57: [49, 56, 58], 58: [50, 57, 59], 59: [58, 60], 60: [52, 59, 61], 61: [53, 60, 62], 62: [54, 61, 63], 63: [55, 62]}
    problem.starts = [22, 48]
    # problem.starts = [27, 25]
    problem.goals = [24, 25]
    problem.n_agents = len(problem.starts)
    for vertex in problem.graph:
        problem.distances[vertex] = dijkstra_distance(problem.graph, vertex)
    print(solver3(problem))
    print(solver1(problem))
    # print(solver2(problem))
