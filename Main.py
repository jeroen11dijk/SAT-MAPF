import itertools

from MAXSATSolverCombined import SATSolverCombined
from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


if __name__ == '__main__':
    problem = BaseProblem("waypoints8_3.graph", "waypoints8_3/4a_6.scen")
    print(SATSolverWaypoints(problem).solve_cnf())
    print(SATSolverWaypoints(problem).solve_cnf(True))
