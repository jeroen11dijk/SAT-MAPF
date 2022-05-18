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
    problem = BaseProblem(5, 1, 5, 0.4)
    # problem.starts = [item for sublist in problem.starts for item in sublist]
    # problem.goals = [item for sublist in problem.goals for item in sublist]
    print(problem.starts)
    print(problem.goals)
    print(MaxSAT(problem))
    print(SAT(problem))

