from MAXSATSolverWaypoints import MAXSATSolverWaypoints
from mstar import Mstar
from problem_classes import BaseProblem

if __name__ == '__main__':
    problem = BaseProblem(4, 1, 8, 0.1)
    print(problem.waypoints)
    res, cost = MAXSATSolverWaypoints(problem).solve(True)
    print(res, cost)
    print(MAXSATSolverWaypoints(problem).solve_cnf())
    print(Mstar(problem.graph, tuple(problem.starts), tuple(problem.waypoints),
                tuple(problem.goals), {}).solve())
