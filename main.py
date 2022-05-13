import functools
import multiprocessing.pool
import os

from MAXSATSolver import MAXSATSolver
from StandardSolver import StandardSolver
from problem_classes import BaseProblem
from utils import dijkstra_distance, convert_grid_dict_ints


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
def SAT(problem):
    return StandardSolver(problem).solve()


@timeout(60.0)
def MaxSAT(problem):
    return MAXSATSolver(problem).solve()

@timeout(60.0)
def SATCNF(problem):
    return StandardSolver(problem).solve_cnf()


@timeout(60.0)
def MaxSATCNF(problem):
    return MAXSATSolver(problem).solve_wcnf()


if __name__ == '__main__':
    res = {0: 0, 1: 0, 2: 0, 3:0}
    ten = 0
    for file in os.listdir('shuffleboard_random_25n_5b_5g_0.0r'):
        main_problem = BaseProblem('shuffleboard_random_25n_5b_5g_0.0r.graph', 'shuffleboard_random_25n_5b_5g_0.0r/' + file)
        ten += 1
        for i, func in enumerate([SAT, SATCNF]):
            try:
                func(main_problem)
                res[i] += 1
            except:
                pass
        if ten == 10:
            print(res)
            res = {0: 0, 1: 0, 2: 0, 3:0}
            ten = 0

