from MAXSATSolverCombined import SATSolverCombined
from problem_classes import BaseProblem


if __name__ == '__main__':
    problem = BaseProblem("combined8.graph", "combined8/7a_0.scen")
    print(problem.starts)
    print(problem.goals)
    print(problem.waypoints)
    print(SATSolverCombined(problem).solve_cnf())
    print(SATSolverCombined(problem).solve_cnf(True))
