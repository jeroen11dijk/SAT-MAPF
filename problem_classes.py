from Problem_generator import safe_generate_grid
from utils import convert_grid_dict_ints, dijkstra_distance, dijkstra_predecessor_and_distance, dynamic_tsp


class BaseProblem:
    graph: dict
    n_agents: int
    starts: list
    waypoints: list
    goals: list
    distances: dict

    def __init__(self, *args):
        if len(args) == 2:
            self.get_railway_problem(args[0], args[1])
        elif len(args) == 4:
            self.get_grid_problem(args[0], args[1], args[2], args[3])
        else:
            self.n_agents = -1
            self.graph = {}
            self.starts = []
            self.waypoints = []
            self.goals = []
            self.distances = {}
            self.heuristics = []

    def get_grid_problem(self, n_agents, n_teams, size, walls):
        self.n_agents = n_agents * n_teams
        problem = safe_generate_grid(n_agents, n_teams, size, walls)
        if n_teams == 1:
            # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
            self.goals = [len(problem.grid[0]) * j + i for i, j in
                          [goal for agent_goal in problem.goals for goal in agent_goal]]
            self.starts = [len(problem.grid[0]) * j + i for i, j in
                           [start for agent_start in problem.starts for start in agent_start]]
        else:
            self.goals = [[len(problem.grid[0]) * j + i for i, j in agent_goal] for agent_goal in problem.goals]
            self.starts = [[len(problem.grid[0]) * j + i for i, j in agent_start] for agent_start in problem.starts]
        self.waypoints = []
        for agent in range(self.n_agents):
            agent_waypoints = []
            for waypoints in problem.waypoints[agent]:
                agent_waypoints.append(len(problem.grid[0]) * waypoints[1] + waypoints[0])
            self.waypoints.append(frozenset(agent_waypoints))
        self.graph = convert_grid_dict_ints(problem.grid)
        self.distances = {}
        for vertex in self.graph:
            self.distances[vertex] = dijkstra_distance(self.graph, vertex)

    def get_railway_problem(self, graph_path, scen_path):
        convert = {}
        self.graph = {}
        for i, line in enumerate(open(graph_path).readlines()[3:]):
            convert[line.split()[0]] = i
        for line in open(graph_path).readlines()[3:]:
            self.graph[convert[line.split()[0]]] = [convert[node] for node in line.split()[1:]]
        self.n_agents = int(open(scen_path).readlines()[2].split()[-1])
        self.starts = []
        self.goals = []
        self.waypoints = [[] for _ in range(self.n_agents)]
        lines = open(scen_path).read().splitlines()
        types_index = lines.index('types')
        starts_index = lines.index('agents starts')
        goals_index = lines.index('goals')
        waypoint_index = lines.index('waypoints')
        for i, line in enumerate(lines[types_index+1:starts_index]):
            self.starts.append([])
            self.goals.append([])
            for agent in line.split()[1:]:
                agent = int(agent)
                self.starts[i].append(convert[lines[starts_index+1+agent].split()[-1]])
                self.goals[i].append(convert[lines[goals_index+1+agent].split()[-1]])
                waypoints = lines[waypoint_index+1+agent].split()
                if len(waypoints) > 1:
                    for waypoint in waypoints[1:]:
                        self.waypoints[agent].append(convert[waypoint])
                    self.waypoints[agent] = frozenset(self.waypoints[agent])
                else:
                    self.waypoints[agent] = frozenset
        if len(self.starts) == self.n_agents:
            self.starts = [item for sublist in self.starts for item in sublist]
            self.goals = [item for sublist in self.goals for item in sublist]
        self.distances = {}
        for vertex in [item for sublist in self.goals for item in sublist]:
            self.distances[vertex] = dijkstra_distance(self.graph, vertex)

class MAPFW:
    def __init__(self):
        self.graph = {}
        self.n_agents = 0
        self.starts = []
        self.goals = []
        self.waypoints = []
        self.heuristic = float("inf")

    def update(self, main, match):
        self.n_agents = main.n_agents
        self.graph = main.graph
        self.waypoints = main.waypoints
        for team in match:
            for agent in team:
                self.starts.append(agent[0])
                self.goals.append(agent[1])

    def get_heuristic(self, distances):
        for i in range(self.n_agents):
            if self.goals[i] not in distances:
                _, distance = dijkstra_predecessor_and_distance(self.graph, self.goals[i])
                distances[self.goals[i]] = distance
            self.heuristic = distances[self.goals[i]][self.starts[i]]