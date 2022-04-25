from StandardSolver import StandardSolver
from MAXSATSolver import MAXSATSolver
from problem_classes import BaseProblem

if __name__ == '__main__':
    problem = BaseProblem(4, 1, 8, 0.01)
    StandardSolver(problem).solve()
    MAXSATSolver(problem).solve()
