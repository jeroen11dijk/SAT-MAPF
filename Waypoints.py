from MAXSATSolverColored import SATSolverColored
from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem
import time
import random
from utils import dynamic_tsp

if __name__ == '__main__':
    problem = BaseProblem("waypoints8_3.graph", "waypoints8_3/5a_0.scen")
    print(SATSolverWaypoints(problem).solve_cnf())
    print(SATSolverWaypoints(problem).solve_cnf(True))
