import functools
import multiprocessing.pool

from pysat.solvers import Glucose3

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
    problem.graph = convert_grid_dict_ints([[0,0], [0,0]])
    problem.starts = [0, 2]
    problem.goals = [1, 3]
    problem.n_agents = len(problem.starts)
    for vertex in problem.graph:
        problem.distances[vertex] = dijkstra_distance(problem.graph, vertex)
    cnf = StandardSolver(problem).generate_dimacs(1)
    solver = Glucose3()
    solver.append_formula(cnf)
    solver.solve()
    print(solver.get_model())
