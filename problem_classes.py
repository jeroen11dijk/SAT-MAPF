from Problem_generator import safe_generate_grid
from utils import convert_grid_dict_ints, dijkstra_distance


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

    def get_grid_problem(self, n_agents, n_teams, size, walls):
        self.n_agents = n_agents * n_teams
        problem = safe_generate_grid(n_agents, n_teams, size, walls)
        print(problem.waypoints)
        self.starts = [len(problem.grid[0]) * j + i for i, j in
                       [start for agent_start in problem.starts for start in agent_start]]
        if n_teams == 1:
            # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
            self.goals = [len(problem.grid[0]) * j + i for i, j in
                          [goal for agent_goal in problem.goals for goal in agent_goal]]
        else:
            self.goals = [[len(problem.grid[0]) * j + i for i, j in agent_goal] for agent_goal in problem.goals]
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
        for line in open(scen_path).readlines()[5 + self.n_agents:5 + 2*self.n_agents]:
            self.starts.append(convert[line.split()[-1]])
        for line in open(scen_path).readlines()[6 + 2*self.n_agents:]:
            self.goals.append(convert[line.split()[-1]])
        self.distances = {}
        for vertex in self.graph:
            self.distances[vertex] = dijkstra_distance(self.graph, vertex)


class ColoredProblem:
    graph: dict
    n_agents: int
    starts: list
    options: dict
    distances: dict
    heuristics: dict
    makespan: int

    def __init__(self, n_agents, graph, starts, options, distances, heuristics, makespan):
        self.n_agents = n_agents
        self.graph = graph
        self.starts = starts
        self.options = options
        self.distances = distances
        self.heuristics = heuristics
        self.makespan = makespan