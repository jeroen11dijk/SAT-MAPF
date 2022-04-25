import functools
import multiprocessing.pool

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


@timeout(5.0)
def solver():
    problem = BaseProblem(8, 1, 5, 0.1)
    StandardSolver(problem).solve()


if __name__ == '__main__':
    solver()
