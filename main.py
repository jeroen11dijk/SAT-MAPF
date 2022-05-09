import functools
import multiprocessing.pool

from MAXSATSolver import MAXSATSolver
from MAXSATSolverUpper import MAXSATSolverUpper
from StandardSolver import StandardSolver
from WMStar.mstar import Mstar
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
    problem = BaseProblem()
    grid = [[1, 0, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    graph = {26: [27], 27: [26, 35, 28], 28: [27, 36], 35: [27, 43, 36], 36: [28, 35, 37], 37: [36], 43: [35, 51], 51: [43, 59], 53: [61], 59: [51, 60], 60: [59, 61], 61: [53, 60]}
    problem.graph = graph
    problem.starts = [28, 53, 37]
    problem.goals = [36, 26, 51]
    problem.n_agents = len(problem.starts)
    for vertex in problem.graph:
        problem.distances[vertex] = dijkstra_distance(problem.graph, vertex)
    print(solver1(problem))
    print(solver0(problem))
    print(solver2(problem))
