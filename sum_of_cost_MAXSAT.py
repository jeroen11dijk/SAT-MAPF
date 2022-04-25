from ortools.sat.python import cp_model

# From https://dl.acm.org/doi/pdf/10.3233/978-1-61499-672-9-810
from problem_classes import SAT_MDD_Problem_Maxsat


def sum_of_cost_sat_mdd_maxsat(problem: SAT_MDD_Problem_Maxsat):
    # Start SAT
    T = range(problem.upperbound)
    vertices = {}
    edges = {}
    time_edges = {}
    model = cp_model.CpModel()
    mdd_vertices = {}
    mdd_edges = {}
    for a in range(problem.n_agents):
        mdd_vertices[a] = {}
        mdd_vertices[a][problem.upperbound] = {problem.goals[a]}
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
                if (t, j, k) not in time_edges:
                    time_edges[t, j, k] = model.NewBoolVar('time_edges[%i, %i, %i]' % (t, j, k,))
    print(len(edges), len(time_edges))
    # Start / End
    for a in range(problem.n_agents):
        model.Add(vertices[0, problem.starts[a], a] == 1)
        vertices[problem.upperbound, problem.goals[a], a] = model.NewBoolVar(
            'vertices[%i, %i, %i]' % (problem.upperbound, problem.goals[a], a))
        model.Add(vertices[problem.upperbound, problem.goals[a], a] == 1)
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
                # If an agent takes an edge add it to time edges so we can minimize it
                if j != k or j != problem.goals[a]:
                    model.AddImplication(edges[t, j, k, a], time_edges[t, j, k])
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
    print("Solve time")
    solver = cp_model.CpSolver()
    model.Minimize(sum(time_edges[key] for key in time_edges))
    status = solver.Solve(model)
    return status, solver, vertices
