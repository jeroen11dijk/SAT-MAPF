from MAXSATSolverCombined import SATSolverCombined
from problem_classes import BaseProblem


if __name__ == '__main__':
    problem = BaseProblem("combined8.graph", "combined8/4a_0.scen")
    print(problem.graph)
    problem.starts = [[25, 30], [20]]
    problem.goals = [[53, 50], [10]]
    problem.n_agents = 3
    print(problem.starts)
    print(problem.goals)
    print(problem.waypoints)
    print(SATSolverCombined(problem).solve_cnf())
    print(SATSolverCombined(problem).solve_cnf(True))
