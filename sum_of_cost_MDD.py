from collections import defaultdict

from ortools.sat.python import cp_model


# From https://dl.acm.org/doi/pdf/10.3233/978-1-61499-672-9-810


def sum_of_cost_sat_mdd(problem):
    # Start SAT
    T = range(problem.mu)
    vertices = {}
    edges = {}
    costs = {}
    model = cp_model.CpModel()
    mdd_vertices = {}
    mdd_edges = {}
    for a in range(problem.n_agents):
        mdd_vertices[a] = {}
        mdd_vertices[a][problem.mu] = {problem.goals[a]}
        mdd_edges[a] = {}
        for t in T:
            mdd_vertices[a][t] = set()
            mdd_edges[a][t] = set()
        for key, value in problem.mdd[a].mdd.items():
            j, t = key
            vertices[t, j, a] = model.NewBoolVar('vertices[%i, %i, %i]' % (t, j, a))
            mdd_vertices[a][t].add(j)
            for nbr in value:
                k = nbr[0]
                mdd_edges[a][t].add((j, k))
                edges[t, j, k, a] = model.NewBoolVar('edges[%i, %i, %i, %i]' % (t, j, k, a))
                if t >= problem.heuristic[a] and (j != k or j != problem.goals[a]):
                    costs[t, a, j, k] = model.NewBoolVar('cost[%i, %i, %i, %i]' % (t, a, j, k))
    # Start / End
    for a in range(problem.n_agents):
        model.Add(vertices[0, problem.starts[a], a] == 1)
        vertices[problem.mu, problem.goals[a], a] = model.NewBoolVar('vertices[%i, %i, %i]' % (problem.mu, problem.goals[a], a))
        model.Add(vertices[problem.mu, problem.goals[a], a] == 1)
    # Constraints
    for a in range(problem.n_agents):
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
                        edges[t, k, j, a2].Not() for a2 in range(problem.n_agents) if
                        a != a2 and (k, j) in mdd_edges[a2][t]).OnlyEnforceIf(
                        edges[t, j, k, a])
            for a2 in range(problem.n_agents):
                if a != a2:
                    for j in mdd_vertices[a][t]:
                        # 5
                        if j in mdd_vertices[a2][t]:
                            model.AddBoolOr(vertices[t, j, a].Not(), vertices[t, j, a2].Not())
            if t >= problem.heuristic[a]:
                for j, k in mdd_edges[a][t]:
                    # 6
                    if (t, a, j, k) in costs:
                        model.AddImplication(edges[t, j, k, a], costs[t, a, j, k])
    # 7
    model.Add(sum(costs[key] for key in costs) <= problem.delta)
    print("Solve time")
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    return status, solver, vertices
