import sys

from MAXSATSolverWaypoints import SATSolverWaypoints
from WMStar.mstar import Mstar
from problem_classes import BaseProblem

if __name__ == "__main__":
    graph = sys.argv[1]
    scen = sys.argv[2]
    algorithm = sys.argv[3]
    problem = BaseProblem(graph, scen)
    if len(open("results_waypoints/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()) > 1:
        prev_agents = int(
            open("results_waypoints/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()[-2].split(
                "a")[0])
        prev_suffix = int(
            open("results_waypoints/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt').readlines()[-2].split(
                "_")[1].split(".")[0])
    else:
        prev_agents = int(scen.split("/")[1].split("a")[0])
        prev_suffix = int(scen.split("/")[1].split("_")[1].split(".")[0]) - 1
    curr_agents = int(scen.split("/")[1].split("a")[0])
    curr_suffix = int(scen.split("/")[1].split("_")[1].split(".")[0])
    same_agents = curr_agents == prev_agents and curr_suffix > prev_suffix
    more_agents = curr_agents - 1 == prev_agents
    if same_agents or more_agents or int(algorithm) == 5:
        file = open("results_waypoints/" + str(graph.split(".")[0]) + "_" + str(algorithm) + '.txt', 'a')
        if int(algorithm) == 1:
            res, cost = SATSolverWaypoints(problem).solve_cnf()
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 2:
            res, cost = SATSolverWaypoints(problem).solve_cnf(True)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 3:
            res, cost = SATSolverWaypoints(problem, inflation=1.25).solve_cnf(True)
            file.write(scen.split("/")[1] + "\n")
            file.write(str(cost) + "\n")
        elif int(algorithm) == 4:
            res, cost = Mstar(problem.graph, tuple(problem.starts), tuple(problem.waypoints), tuple(problem.goals),
                              {}).solve()
            file.write(scen.split("/")[1] + "\n")
    else:
        print("skip")
