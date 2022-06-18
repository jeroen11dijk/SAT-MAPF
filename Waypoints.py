from MAXSATSolverColored import SATSolverColored
from MAXSATSolverWaypoints import MAXSATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem
import time
import random
from utils import dynamic_tsp

if __name__ == '__main__':
    problem = BaseProblem("grid8_1.graph", "grid8_1/38a_0.scen")
    print(SATSolverColored(problem).solve_cnf())
    print(SATSolverColored(problem).solve_cnf(True))
