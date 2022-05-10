import itertools

from MAXSATSolverColored import MAXSATSolverColored
from MAXSATSolverWaypoints import MAXSATSolverWaypoints
from Problem_generator import safe_generate_grid
from mstar import Mstar
from problem_classes import ColoredProblem, WaypointProblem
from utils import convert_grid_dict_ints, dijkstra_distance, dynamic_tsp

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    starts = [0, 8]
    n_agents = 2
    waypoints = ((7,), (0,))
    goals = [4, 3]
    graph = convert_grid_dict_ints(grid)
    distances = {}
    for vertex in graph:
        distances[vertex] = dijkstra_distance(graph, vertex)
    options = {}
    makespans = []
    heuristics = []
    # Loop over agents and calculate individual heuristic which we will sum at the end
    tsp_cache = {}
    for i in range(n_agents):
        current = starts[i]
        agent_waypoints = waypoints[i]
        goal = goals[i]
        if len(agent_waypoints) == 0:
            heuristics.append(distances[goal][current])
        elif len(agent_waypoints) == 1:
            heuristics.append(distances[goal][list(agent_waypoints)[0]] + distances[list(agent_waypoints)[0]][current])
        else:
            tsp = dynamic_tsp(agent_waypoints, goal, distances, tsp_cache)
            min_dist = float("inf")
            for coord in tsp:
                dist = tsp[coord] + distances[coord][current]
                min_dist = min(min_dist, dist)
            heuristics.append(min_dist)

    res, cost = MAXSATSolverWaypoints(WaypointProblem(n_agents, graph, starts, goals, waypoints, distances, heuristics, max(heuristics))).solve()
    print(res, cost)
    print(Mstar(graph, tuple(starts), tuple(waypoints), tuple(goals), {}).solve())