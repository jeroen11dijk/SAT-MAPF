from ortools.sat.python import cp_model

from MDD import MDD
from problem_classes import BaseProblem


class StandardSolver(BaseProblem):

    def __init__(self, *args):
        super().__init__(*args)
        self.heuristic = {}
        for agent in range(self.n_agents):
            self.heuristic[agent] = self.distances[self.goals[agent]][self.starts[agent]]
        self.min_makespan = max(self.heuristic.values())
        self.delta = 0
        self.mdd = {}
        for a in range(self.n_agents):
            self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], self.min_makespan)

    def solve(self):
        while True:
            mu = self.min_makespan + self.delta
            for a in range(self.n_agents):
                if self.delta > 0:
                    self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], mu, self.mdd[a])
            status, solver, path = self.SAT_solver(mu)
            if status == 4:
                break
            self.delta += 1
        res = [[] for _ in range(mu + 1)]
        cost = 0
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
                if key[1] != self.goals[key[2]]:
                    cost += 1
        print(res, cost)

    def SAT_solver(self, mu):
        T = range(mu)
        vertices = {}
        edges = {}
        costs = {}
        model = cp_model.CpModel()
        mdd_vertices = {}
        mdd_edges = {}
        for a in range(self.n_agents):
            mdd_vertices[a] = {}
            mdd_vertices[a][mu] = {self.goals[a]}
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
                    if t >= self.heuristic[a] and (j != k or j != self.goals[a]):
                        costs[t, a, j, k] = model.NewBoolVar('cost[%i, %i, %i, %i]' % (t, a, j, k))
        # Start / End
        for a in range(self.n_agents):
            model.Add(vertices[0, self.starts[a], a] == 1)
            vertices[mu, self.goals[a], a] = model.NewBoolVar(
                'vertices[%i, %i, %i]' % (mu, self.goals[a], a))
            model.Add(vertices[mu, self.goals[a], a] == 1)
        # Constraints
        for a in range(self.n_agents):
            for t in T:
                # No two agents at a vertex at timestep t
                model.Add(sum(vertices[t, j, a] for j in mdd_vertices[a][t]) == 1)
                for j in mdd_vertices[a][t]:
                    # 1
                    model.AddBoolOr([edges[t, j, l, a] for k, l in mdd_edges[a][t] if j == k]).OnlyEnforceIf(
                        vertices[t, j, a])
                for j, k in mdd_edges[a][t]:
                    # 3
                    model.AddBoolAnd(vertices[t, j, a], vertices[t + 1, k, a]).OnlyEnforceIf(edges[t, j, k, a])
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
                if t >= self.heuristic[a]:
                    for j, k in mdd_edges[a][t]:
                        # 6
                        if (t, a, j, k) in costs:
                            model.AddImplication(edges[t, j, k, a], costs[t, a, j, k])
        # 7
        model.Add(sum(costs[key] for key in costs) <= self.delta)
        print("Solve time")
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        return status, solver, vertices