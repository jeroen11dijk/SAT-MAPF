import itertools

from ortools.sat.python import cp_model
from pysat.card import CardEnc
from pysat.formula import CNF
from pysat.solvers import Glucose3
from datetime import datetime
from MDD import MDD


class SATSolverColored:

    def __init__(self, problem, inflation=1):
        self.graph = problem.graph
        self.n_agents = problem.n_agents
        self.starts = problem.starts
        self.options = {}
        makespans = []
        self.heuristics = []
        for team in zip(problem.starts, problem.goals):
            for start in team[0]:
                self.options[start] = team[1]
            opt = float('inf')
            makespan = float('inf')
            for matching in [list(zip(perm, team[1])) for perm in itertools.permutations(team[0], len(team[1]))]:
                heuristic = []
                invalid_match = False
                for match in matching:
                    try:
                        heuristic.append(problem.distances[match[1]][match[0]])
                    except:
                        invalid_match = True
                        break
                if not invalid_match and sum(heuristic) < opt:
                    opt = sum(heuristic)
                    makespan = max(heuristic)
            makespans.append(makespan)
            self.heuristics.append(opt)
        self.min_makespan = round(max(makespans) * inflation)
        self.starts = [item for sublist in problem.starts for item in sublist]
        self.delta = 0
        self.mdd = {}
        for a in range(self.n_agents):
            self.mdd[a] = MDD(self.graph, a, self.starts[a], self.options[self.starts[a]], self.min_makespan)

    def solve(self, minimize):
        while True:
            mu = self.min_makespan + self.delta
            for a in range(self.n_agents):
                if self.delta > 0:
                    self.mdd[a] = MDD(self.graph, a, self.starts[a], self.options[self.starts[a]], mu, self.mdd[a])
            status, solver, path = self.MAXSAT_solver(mu, minimize)
            if status == 4:
                break
            self.delta += 1
        res = [[] for _ in range(mu + 1)]
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
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

    def MAXSAT_solver(self, upperbound, minimize):
        T = range(upperbound)
        vertices = {}
        edges = {}
        waiting = {}
        model = cp_model.CpModel()
        mdd_vertices = {}
        mdd_edges = {}
        for a in range(self.n_agents):
            mdd_vertices[a] = {}
            mdd_vertices[a][upperbound] = {goal for goal in self.options[self.starts[a]]}
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
                    if j == k and j in self.options[self.starts[a]]:
                        waiting[t, j, k, a] = model.NewBoolVar('waiting[%i, %i, %i, %i]' % (t, j, k, a))
        # Start / End
        for a in range(self.n_agents):
            model.Add(vertices[0, self.starts[a], a] == 1)
            for goal in self.options[self.starts[a]]:
                vertices[upperbound, goal, a] = model.NewBoolVar(
                    'vertices[%i, %i, %i]' % (upperbound, goal, a))
            model.AddBoolOr([vertices[upperbound, goal, a] for goal in self.options[self.starts[a]]])
        # Constraints
        for a in range(self.n_agents):
            # No two agents at a vertex at the final timestep
            model.Add(sum(vertices[upperbound, j, a] for j in mdd_vertices[a][upperbound]) == 1)
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
                    # If an agent waites on a target location add it to waiting so we can maximise it
                    if j == k and j in self.options[self.starts[a]]:
                        model.AddBoolAnd([edges[t, j, k, a]] + [vertices[t2, j, a] for t2 in range(t, upperbound+1)]).OnlyEnforceIf(
                            waiting[t, j, k, a])
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
                        if t == upperbound - 1:
                            for j in mdd_vertices[a][upperbound]:
                                # 5
                                if j in mdd_vertices[a2][upperbound]:
                                    model.AddBoolOr(vertices[upperbound, j, a].Not(), vertices[upperbound, j, a2].Not())
        if minimize:
            model.Maximize(sum(waiting[key] for key in waiting))
        else:
            waiting_moves = (self.n_agents * upperbound) - (sum(self.heuristics) + self.delta)
            model.Add(sum(waiting[key] for key in waiting) == waiting_moves)
        print("Solve time:" + str(datetime.now()))
        solver = cp_model.CpSolver()
        print("Done solving:" + str(datetime.now()))
        status = solver.Solve(model)
        return status, solver, vertices

    def solve_cnf(self):
        while True:
            mu = self.min_makespan + self.delta
            for a in range(self.n_agents):
                if self.delta > 0:
                    self.mdd[a] = MDD(self.graph, a, self.starts[a], self.options[self.starts[a]], mu, self.mdd[a])
            cnf, convert = self.generate_cnf(mu)
            solver = Glucose3()
            solver.append_formula(cnf)
            solver.solve()
            if solver.get_model() is not None:
                break
            self.delta += 1
        path = set()
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
        waiting = {}
        time_edges = {}
        mdd_vertices = {}
        mdd_edges = {}
        for a in range(self.n_agents):
            mdd_vertices[a] = {}
            mdd_vertices[a][upperbound] = {goal for goal in self.options[self.starts[a]]}
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
                    if j == k and j in self.options[self.starts[a]]:
                        waiting[t, j, k, a] = index = index + 1
                    if (t, j, k) not in time_edges:
                        time_edges[t, j, k] = index = index + 1
        # Start / End
        for a in range(self.n_agents):
            cnf.append([vertices[0, self.starts[a], a]])
            for goal in self.options[self.starts[a]]:
                vertices[upperbound, goal, a] = index = index + 1
            cnf.append([vertices[upperbound, goal, a] for goal in self.options[self.starts[a]]])
        # Constraints
        for a in range(self.n_agents):
            # No two agents at a vertex at the final timestep
            cnf.extend(CardEnc.atmost(lits=[vertices[upperbound, key, a] for key in mdd_vertices[a][upperbound]],
                                      top_id=cnf.nv, bound=1))
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
                    # If an agent takes an edge add it to time edges so we can minimize it
                    if j == k and j in self.options[self.starts[a]]:
                        cnf.append([-waiting[t, j, k, a], edges[t, j, k, a]])
                        for t2 in range(t, upperbound + 1):
                            cnf.append([-waiting[t, j, k, a], vertices[t2, j, a]])
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
                        if t == upperbound - 1:
                            for j in mdd_vertices[a][upperbound]:
                                # 5
                                if j in mdd_vertices[a2][upperbound]:
                                    cnf.append([-vertices[upperbound, j, a], -vertices[upperbound, j, a2]])
        bound = (self.n_agents * upperbound) - (sum(self.heuristics) + self.delta)
        cardinality = CardEnc.atleast(lits=[waiting[key] for key in waiting], top_id=cnf.nv, bound=bound)
        cnf.extend(cardinality.clauses)
        return cnf, {v: k for k, v in vertices.items()}
