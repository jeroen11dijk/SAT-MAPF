from ortools.sat.python import cp_model

from MDD import MDD
from utils import dijkstra_distance, dynamic_tsp


class MAXSATSolverWaypoints:

    def __init__(self, problem):
        self.graph = problem.graph
        self.n_agents = problem.n_agents
        self.starts = problem.starts
        self.goals = problem.goals
        self.waypoints = problem.waypoints
        self.distances = problem.distances
        self.heuristics = []
        tsp_cache = {}
        for i in range(self.n_agents):
            current = self.starts[i]
            agent_waypoints = self.waypoints[i]
            goal = self.goals[i]
            if len(agent_waypoints) == 0:
                self.heuristics.append(self.distances[goal][current])
            elif len(agent_waypoints) == 1:
                self.heuristics.append(
                    self.distances[goal][list(agent_waypoints)[0]] + self.distances[list(agent_waypoints)[0]][current])
            else:
                tsp = dynamic_tsp(agent_waypoints, goal, self.distances, tsp_cache)
                min_dist = float("inf")
                for coord in tsp:
                    dist = tsp[coord] + self.distances[coord][current]
                    min_dist = min(min_dist, dist)
                self.heuristics.append(min_dist)
        self.min_makespan = max(self.heuristics)
        self.delta = 0
        self.mdd = {}
        # TODO waypoints MDD
        for a in range(self.n_agents):
            self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], self.min_makespan)

    def solve(self):
        while True:
            mu = self.min_makespan + self.delta
            for a in range(self.n_agents):
                if self.delta > 0:
                    self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], mu, self.mdd[a])
            status, solver, path = self.MAXSAT_solver(mu)
            if status == 4:
                break
            self.delta += 1
        res = [[] for _ in range(mu + 1)]
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
        cost = (mu+1)*self.n_agents
        waiting = {i for i in range(self.n_agents)}
        for locations in reversed(res):
            for a in range(len(locations)):
                if a in waiting and locations[a] == self.goals[a]:
                    cost -= 1
                if a in waiting and locations[a] != self.goals[a]:
                    waiting.remove(a)
        return res, cost

    def MAXSAT_solver(self, upperbound):
        T = range(upperbound)
        vertices = {}
        edges = {}
        time_edges = {}
        model = cp_model.CpModel()
        mdd_vertices = {}
        mdd_edges = {}
        for a in range(self.n_agents):
            mdd_vertices[a] = {}
            mdd_vertices[a][upperbound] = {self.goals[a]}
            mdd_edges[a] = {}
            for t in T:
                mdd_vertices[a][t] = set()
                mdd_edges[a][t] = set()
            for key, value in self.mdd[a].mdd.items():
                j, t = key
                vertices[t, j, a] = model.NewBoolVar('vertices[%i, %i, %i]' % (t, j, a))
                mdd_vertices[a][t].add(j)
                for nbr in value:
                    k = nbr[0]
                    mdd_edges[a][t].add((j, k))
                    edges[t, j, k, a] = model.NewBoolVar('edges[%i, %i, %i, %i]' % (t, j, k, a))
                    if (t, j, k) not in time_edges:
                        time_edges[t, j, k] = model.NewBoolVar('time_edges[%i, %i, %i]' % (t, j, k,))
        # Start / End
        for a in range(self.n_agents):
            model.Add(vertices[0, self.starts[a], a] == 1)
            vertices[upperbound, self.goals[a], a] = model.NewBoolVar(
                'vertices[%i, %i, %i]' % (upperbound, self.goals[a], a))
            model.Add(vertices[upperbound, self.goals[a], a] == 1)
            for waypoint in self.waypoints[a]:
                model.AddBoolOr([vertices[t, waypoint, a] for t in range(1, upperbound) if waypoint in mdd_vertices[a][t]])
        # Constraints
        for a in range(self.n_agents):
            for t in T:
                # No two agents at a vertex at timestep t
                model.Add(sum(vertices[t, j, a] for j in mdd_vertices[a][t]) == 1)
                for j in mdd_vertices[a][t]:
                    # 1
                    model.AddBoolOr([edges[t, j, l, a] for k, l in mdd_edges[a][t] if j == k]).OnlyEnforceIf(
                        vertices[t, j, a])
                    # Agents cant move from the target
                    if j == self.goals[a]:
                        model.AddImplication(vertices[t, j, a], edges[t, j, j, a])
                for j, k in mdd_edges[a][t]:
                    # 3
                    model.AddBoolAnd(vertices[t, j, a], vertices[t + 1, k, a]).OnlyEnforceIf(edges[t, j, k, a])
                    # If an agent takes an edge add it to time edges so we can minimize it
                    if j != k or j != self.goals[a]:
                        model.AddImplication(edges[t, j, k, a], time_edges[t, j, k])
                    if j != k:
                        # 4 edited so the edges must be empty
                        model.AddBoolAnd(
                            edges[t, k, j, a2].Not() for a2 in range(self.n_agents) if
                            a != a2 and (k, j) in mdd_edges[a2][t]).OnlyEnforceIf(
                            edges[t, j, k, a])
                for a2 in range(self.n_agents):
                    if a != a2:
                        for j in mdd_vertices[a][t]:
                            # 5
                            if j in mdd_vertices[a2][t]:
                                model.AddBoolOr(vertices[t, j, a].Not(), vertices[t, j, a2].Not())
        model.Add(sum(time_edges[key] for key in time_edges) <= sum(self.heuristics) + self.delta)
        solver = cp_model.CpSolver()
        # model.Minimize(sum(time_edges[key] for key in time_edges))
        status = solver.Solve(model)
        return status, solver, vertices
