from pysat.card import CardEnc
from pysat.examples.rc2 import RC2
from pysat.formula import CNF, WCNF
from pysat.solvers import Glucose3

from MDD import MDD


class SATSolver:

    def __init__(self, problem, inflation=1):
        self.graph = problem.graph
        self.n_agents = problem.n_agents
        self.starts = problem.starts
        self.goals = problem.goals
        self.distances = problem.distances
        self.heuristics = problem.heuristics
        self.min_makespan = round(max(self.heuristics) * inflation)
        self.delta = 0
        self.mdd = {}
        for a in range(self.n_agents):
            self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], self.min_makespan)

    def solve_cnf(self, maxsat=False):
        while True:
            mu = self.min_makespan + self.delta
            for a in range(self.n_agents):
                if self.delta > 0:
                    self.mdd[a] = MDD(self.graph, a, self.starts[a], self.goals[a], mu, self.mdd[a])
            if maxsat:
                wcnf, convert = self.generate_wcnf(mu)
                rc2 = RC2(wcnf)
                model = rc2.compute()
                if model is not None:
                    break
            else:
                cnf, convert = self.generate_cnf(mu)
                solver = Glucose3()
                solver.append_formula(cnf)
                solver.solve()
                if solver.get_model() is not None:
                    break
            self.delta += 1
        path = set()
        if maxsat:
            for clause in model:
                if clause in convert:
                    path.add(convert[clause])
        else:
            for clause in solver.get_model():
                if clause in convert:
                    path.add(convert[clause])
        res = [[] for _ in range(mu + 1)]
        for key in sorted(path, key=lambda x: (x[0], x[2])):
            res[key[0]].append(key[1])
        cost = (mu + 1) * self.n_agents
        waiting = {i for i in range(self.n_agents)}
        goals = res[-1]
        for locations in reversed(res):
            for a in range(len(locations)):
                if a in waiting and locations[a] == goals[a]:
                    cost -= 1
                if a in waiting and locations[a] != goals[a]:
                    waiting.remove(a)
        return res, cost

    def generate_cnf(self, upperbound):
        cnf = CNF()
        index = 0
        T = range(upperbound)
        vertices = {}
        edges = {}
        costs = {}
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
                vertices[t, j, a] = index = index + 1
                mdd_vertices[a][t].add(j)
                for nbr in value:
                    k = nbr[0]
                    mdd_edges[a][t].add((j, k))
                    edges[t, j, k, a] = index = index + 1
                    if t >= self.heuristics[a] and (j != k or j != self.goals[a]):
                        costs[t, a, j, k] = index = index + 1
        # Start / End
        for a in range(self.n_agents):
            cnf.append([vertices[0, self.starts[a], a]])
            vertices[upperbound, self.goals[a], a] = index = index + 1
            cnf.append([vertices[upperbound, self.goals[a], a]])
        # Constraints
        for a in range(self.n_agents):
            for t in T:
                # No two agents at a vertex at timestep t
                cnf.extend(
                    CardEnc.atmost(lits=[vertices[t, key, a] for key in mdd_vertices[a][t]], top_id=cnf.nv, bound=1))
                for j in mdd_vertices[a][t]:
                    # 1
                    cnf.append([-vertices[t, j, a]] + [edges[t, j, l, a] for k, l in mdd_edges[a][t] if j == k])
                for j, k in mdd_edges[a][t]:
                    # 3
                    cnf.append([-edges[t, j, k, a], vertices[t, j, a]])
                    cnf.append([-edges[t, j, k, a], vertices[t + 1, k, a]])
                    if j != k:
                        # 4 edited so the edges must be empty
                        for a2 in range(self.n_agents):
                            if a != a2 and (k, j) in mdd_edges[a2][t]:
                                cnf.append([-edges[t, j, k, a], -edges[t, k, j, a2]])
                for a2 in range(self.n_agents):
                    if a != a2:
                        for j in mdd_vertices[a][t]:
                            # 5
                            if j in mdd_vertices[a2][t]:
                                cnf.append([-vertices[t, j, a], -vertices[t, j, a2]])
                if t >= self.heuristics[a]:
                    for j, k in mdd_edges[a][t]:
                        # 6
                        if (t, a, j, k) in costs:
                            cnf.append([-edges[t, j, k, a], costs[t, a, j, k]])
        cardinality = CardEnc.atmost(lits=[costs[key] for key in costs], top_id=cnf.nv,
                                      bound=self.delta)
        cnf.extend(cardinality.clauses)
        return cnf, {v: k for k, v in vertices.items()}

    def generate_wcnf(self, upperbound):
        wcnf = WCNF()
        index = 0
        T = range(upperbound)
        vertices = {}
        edges = {}
        costs = {}
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
                vertices[t, j, a] = index = index + 1
                mdd_vertices[a][t].add(j)
                for nbr in value:
                    k = nbr[0]
                    mdd_edges[a][t].add((j, k))
                    edges[t, j, k, a] = index = index + 1
                    if t >= self.heuristics[a] and (j != k or j != self.goals[a]):
                        costs[t, a, j, k] = index = index + 1
                        wcnf.append([-costs[t, a, j, k]], weight=1)
        # Start / End
        for a in range(self.n_agents):
            wcnf.append([vertices[0, self.starts[a], a]])
            vertices[upperbound, self.goals[a], a] = index = index + 1
            wcnf.append([vertices[upperbound, self.goals[a], a]])
        # Constraints
        for a in range(self.n_agents):
            for t in T:
                # No two agents at a vertex at timestep t
                wcnf.extend(
                    CardEnc.atmost(lits=[vertices[t, key, a] for key in mdd_vertices[a][t]], top_id=wcnf.nv, bound=1))
                for j in mdd_vertices[a][t]:
                    # 1
                    wcnf.append([-vertices[t, j, a]] + [edges[t, j, l, a] for k, l in mdd_edges[a][t] if j == k])
                for j, k in mdd_edges[a][t]:
                    # 3
                    wcnf.append([-edges[t, j, k, a], vertices[t, j, a]])
                    wcnf.append([-edges[t, j, k, a], vertices[t + 1, k, a]])
                    if j != k:
                        # 4 edited so the edges must be empty
                        for a2 in range(self.n_agents):
                            if a != a2 and (k, j) in mdd_edges[a2][t]:
                                wcnf.append([-edges[t, j, k, a], -edges[t, k, j, a2]])
                for a2 in range(self.n_agents):
                    if a != a2:
                        for j in mdd_vertices[a][t]:
                            # 5
                            if j in mdd_vertices[a2][t]:
                                wcnf.append([-vertices[t, j, a], -vertices[t, j, a2]])
                if t >= self.heuristics[a]:
                    for j, k in mdd_edges[a][t]:
                        # 6
                        if (t, a, j, k) in costs:
                            wcnf.append([-edges[t, j, k, a], costs[t, a, j, k]])
        return wcnf, {v: k for k, v in vertices.items()}