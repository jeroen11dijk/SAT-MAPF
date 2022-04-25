from StandardSolver import StandardSolver
from MAXSATSolver import MAXSATSolver

if __name__ == '__main__':
    StandardSolver(4, 1, 8, 0.01).solve()
    MAXSATSolver(4, 1, 8, 0.01).solve()
