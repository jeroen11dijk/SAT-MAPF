from MAXSATSolverWaypoints import MAXSATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem

if __name__ == '__main__':
    problem = BaseProblem("graph.graph", "problem.scen")
    print(problem.waypoints)
    print(problem.waypoints)
    res, cost = MAXSATSolverWaypoints(problem).solve(True)
    print(res, cost)
    print(MAXSATSolverWaypoints(problem).solve_cnf())
    print(Mstar(problem.graph, tuple(problem.starts), tuple(problem.waypoints),
                tuple(problem.goals), {}).solve())
