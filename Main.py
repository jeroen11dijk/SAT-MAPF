from MAXSATSolverColored import SATSolverColored
from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem
import time
import random
from utils import dynamic_tsp

if __name__ == '__main__':
    problem = BaseProblem("waypoints32_9.graph", "waypoints32_9/4a_3.scen")
    print(SATSolverWaypoints(problem).solve_cnf())
    print(SATSolverWaypoints(problem).solve_cnf(True))
    # print(Mstar(problem.graph, tuple(problem.starts), tuple(problem.waypoints), tuple(problem.goals),
    #                           {}).solve())