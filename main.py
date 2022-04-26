import functools
import multiprocessing.pool

from MAXSATSolver import MAXSATSolver
from MAXSATSolverUpper import MAXSATSolverUpper
from StandardSolver import StandardSolver
from problem_classes import BaseProblem


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
    StandardSolver(problem).solve()


@timeout(60.0)
def solver1(problem):
    MAXSATSolver(problem).solve()


@timeout(60.0)
def solver2(problem):
    MAXSATSolverUpper(problem).solve()


if __name__ == '__main__':
    for a in range(8, 11):
        res = {0: 0, 1: 0, 2: 0}
        for _ in range(10):
            main_problem = BaseProblem(a, 1, 8, 0.1)
            for i, func in enumerate([solver0, solver1, solver2]):
                try:
                    func(main_problem)
                    res[i] += 1
                except:
                    pass
        print(str(a) + ": " + str(res))
