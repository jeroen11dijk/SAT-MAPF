import itertools

from MAXSATSolverCombined import SATSolverCombined
from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


if __name__ == '__main__':
    problem = BaseProblem("combined8.graph", "combined8/4a_6.scen")
    print(SATSolverCombined(problem).solve_cnf())
    print(SATSolverCombined(problem).solve_cnf(True))
