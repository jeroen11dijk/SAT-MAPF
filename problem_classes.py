from dataclasses import dataclass

from MDD import MDD
from Problem_generator import safe_generate_grid
from utils import convert_graph, dijkstra_predecessor_and_distance


class BaseProblem:
    graph: dict
    n_agents: int
    starts: list
    goals: list
    distances: dict

    def __init__(self, *args):
        if len(args) == 2:
            self.get_railway_problem(args[0], args[1])
        elif len(args) == 4:
            self.get_grid_problem(args[0], args[1], args[2], args[3])
        else:
            print("Wrong inputs so default is used!")
            self.get_grid_problem(4, 1, 5, 0.1)

    def get_grid_problem(self, n_agents, n_teams, size, walls):
        self.n_agents = n_agents
        problem = safe_generate_grid(n_agents, n_teams, size, walls)
        # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
        self.starts = [len(problem.grid) * j + i for i, j in
                       [start for agent_start in problem.starts for start in agent_start]]
        self.goals = [len(problem.grid) * j + i for i, j in
                      [goal for agent_goal in problem.goals for goal in agent_goal]]
        self.graph = convert_graph(problem.grid)
        self.distances = {}
        for vertex in self.graph:
            self.distances[vertex] = dijkstra_predecessor_and_distance(self.graph, vertex)

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
        for line in open(scen_path).readlines()[5:5 + self.n_agents]:
            self.starts.append(convert[line.split()[-1]])
        for line in open(scen_path).readlines()[6 + self.n_agents:]:
            self.goals.append(convert[line.split()[-1]])
        self.distances = {}
        for vertex in self.graph:
            self.distances[vertex] = dijkstra_predecessor_and_distance(self.graph, vertex)


class StandardSolver(BaseProblem):

    def __init__(self, *args):
        super().__init__(*args)
        self.heuristic = {}
        for agent in range(self.n_agents):
            self.heuristic[agent] = self.distances[self.goals[agent]][self.starts[agent]]
        self.mu = max(self.heuristic.values())
        self.delta = 0
        self.mdd = {}
        for a in range(self.n_agents):
            self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], self.mu)


