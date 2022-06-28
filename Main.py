import itertools

from MAXSATSolverCombined import SATSolverCombined
from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem, MAPFW


if __name__ == '__main__':
    problem = BaseProblem("grid8.graph", "grid8/4a_6.scen")
    print(problem.graph)
    print(problem.starts)
    print(problem.goals)