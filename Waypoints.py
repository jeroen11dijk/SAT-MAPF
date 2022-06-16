from MAXSATSolverWaypoints import MAXSATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem
import time
import random
from utils import dynamic_tsp

if __name__ == '__main__':
    problem = BaseProblem("grid32.graph", "grid32/4a_0.scen")
    waypoints = tuple(random.sample(problem.graph.keys(), 15))
    tsp_cache = {}
    start = time.time()
    dynamic_tsp(waypoints, problem.goals[0][0], problem.distances, tsp_cache)
    print(time.time() - start)
