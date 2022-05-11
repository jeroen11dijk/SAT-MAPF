from MAXSATSolverColored import MAXSATSolverColored
from mstar import Mstar
from problem_classes import BaseProblem

if __name__ == '__main__':
    problem = BaseProblem(2, 2, 8, 0.1)
    res, cost = MAXSATSolverColored(problem).solve()
    print(res, cost)
    print(Mstar(problem.graph, tuple([0, 5, 8]), ((), (), (), (), (), (), (), (), (), ()),
                tuple([6, 4, 3]), {}).solve())
    print(Mstar(problem.graph, tuple([0, 5, 8]), ((), (), (), (), (), (), (), (), (), ()),
                tuple([4, 6, 3]), {}).solve())
