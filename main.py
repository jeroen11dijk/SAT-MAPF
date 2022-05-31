import functools
import multiprocessing.pool
import time

from func_timeout import func_set_timeout

from MAXSATSolver import MAXSATSolver
from StandardSolver import StandardSolver
from problem_classes import BaseProblem


@func_set_timeout(60.0)
def SAT(problem):
    return StandardSolver(problem).solve()


@func_set_timeout(60.0)
def MaxSAT(problem):
    return MAXSATSolver(problem).solve(True)

@func_set_timeout(60.0)
def MaxSAT2(problem):
    return MAXSATSolver(problem).solve(False)

@func_set_timeout(60.0)
def SATCNF(problem):
    return StandardSolver(problem).solve_cnf()

@func_set_timeout(60.0)
def MaxSATCNF(problem):
    return MAXSATSolver(problem).solve_wcnf()


if __name__ == '__main__':
    problem = BaseProblem(10, 1, 15, 0.1)
    # problem.starts = [item for sublist in problem.starts for item in sublist]
    # problem.goals = [item for sublist in problem.goals for item in sublist]
    start = time.time()
    print(MaxSAT(problem))
    print(time.time() - start)
    # start = time.time()
    # print(MaxSAT2(problem))
    # print(time.time() - start)
    # start = time.time()
    # print(SAT(problem))
    # print(time.time() - start)
    start = time.time()
    print(SATCNF(problem))
    print(time.time() - start)
    start = time.time()
    print(MaxSATCNF(problem))
    print(time.time() - start)
