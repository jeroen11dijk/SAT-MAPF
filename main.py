import time

from graph import get_railway_problem

from MDD import MDD
from problem_classes import SAT_MDD_Problem, SAT_MDD_Problem_Maxsat
from sum_of_cost_MAXSAT import sum_of_cost_sat_mdd_maxsat
from sum_of_cost_MDD import sum_of_cost_sat_mdd

if __name__ == '__main__':
    problem = get_railway_problem('Sjoel.graph', 'S.scen')
    start = time.time()
    heuristic = {}
    for agent in range(problem.n_agents):
        heuristic[agent] = problem.distances[problem.goals[agent]][problem.starts[agent]]
    min_makespan = max(heuristic.values())
    delta = 0
    mdd = {}
    maxsat = True
    if maxsat:
        start = time.time()
        for a in range(problem.n_agents):
            mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], min_makespan)
        while True:
            mu = min_makespan + delta
            for a in range(problem.n_agents):
                if delta > 0:
                    mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], mu, mdd[a])
            status, solver, path = sum_of_cost_sat_mdd_maxsat(
                SAT_MDD_Problem_Maxsat(mdd, problem.n_agents, mu, problem.starts, problem.goals))
            if status == 4:
                break
            delta += 1
        res = [[] for x in range(mu + 1)]
        cost = 0
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
                if key[1] != problem.goals[key[2]]:
                    cost += 1
        print((res, cost))
        print(time.time() - start)
        start = time.time()
        upperbound = round(min_makespan * 1.25)
        print(upperbound)
        for a in range(problem.n_agents):
            mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], upperbound)
        status, solver, path = sum_of_cost_sat_mdd_maxsat(
            SAT_MDD_Problem_Maxsat(mdd, problem.n_agents, upperbound, problem.starts, problem.goals))
        res = [[] for x in range(upperbound + 1)]
        cost = 0
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
                if key[1] != problem.goals[key[2]]:
                    cost += 1
        print((res, cost))
        print(time.time() - start)
    else:
        start = time.time()
        for a in range(problem.n_agents):
            mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], min_makespan)
        while True:
            mu = min_makespan + delta
            for a in range(problem.n_agents):
                if delta > 0:
                    mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], mu, mdd[a])
            status, solver, path = sum_of_cost_sat_mdd_maxsat(
                SAT_MDD_Problem_Maxsat(mdd, problem.n_agents, mu, problem.starts, problem.goals))
            if status == 4:
                break
            delta += 1
        res = [[] for x in range(mu + 1)]
        cost = 0
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
                if key[1] != problem.goals[key[2]]:
                    cost += 1
        print((res, cost))
        print(time.time() - start)
        start = time.time()
        for a in range(problem.n_agents):
            mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], min_makespan)
        while True:
            mu = min_makespan + delta
            for a in range(problem.n_agents):
                if delta > 0:
                    mdd[a] = MDD(problem.graph, a, problem.starts[a], problem.goals[a], mu, mdd[a])
            status, solver, path = sum_of_cost_sat_mdd(
                SAT_MDD_Problem(mdd, problem.n_agents, mu, delta, problem.starts, problem.goals, heuristic))
            if status == 4:
                break
            delta += 1
        res = [[] for x in range(mu + 1)]
        cost = 0
        for key in sorted(path.keys(), key=lambda x: (x[0], x[2])):
            if solver.BooleanValue(path[key]):
                res[key[0]].append(key[1])
                if key[1] != problem.goals[key[2]]:
                    cost += 1
        print((res, cost))
        print(time.time() - start)
