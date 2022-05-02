from mapfmclient import MapfBenchmarker
from mapfmclient import Solution
from mapfw import get_all_benchmarks

from MAXSATSolver import MAXSATSolver
from Mstar_utils import convert_grid_dict_coords
from mstar import Mstar
from problem_classes import BaseProblem
from utils import dijkstra_distance, convert_grid_dict_ints


def solverMstar(problem):
    starts = []
    goals = []
    for start in problem.starts:
        starts.append((start.x, start.y))
    for goal in problem.goals:
        goals.append((goal.x, goal.y))
    paths, cost = Mstar(convert_grid_dict_coords(problem.grid), tuple(starts), ((), (), ()), tuple(goals), {}).solve()
    reverse_paths = [[], [], []]
    for t in paths:
        for a, v in enumerate(t):
            reverse_paths[a].append(v)
    print(reverse_paths)
    return Solution.from_paths(reverse_paths)


def solverMaxSAT(problem):
    main_problem = BaseProblem()
    main_problem.graph = convert_grid_dict_ints(problem.grid)
    main_problem.n_agents = len(problem.starts)
    starts = []
    goals = []
    for start in sorted(problem.starts, key=lambda x: x.color):
        starts.append(([(start.x, start.y)]))
    for goal in sorted(problem.goals, key=lambda x: x.color):
        goals.append(([(goal.x, goal.y)]))
    main_problem.starts = [len(problem.grid[0]) * j + i for i, j in
                           [start for agent_start in starts for start in agent_start]]
    main_problem.goals = [len(problem.grid[0]) * j + i for i, j in
                          [goal for agent_goal in goals for goal in agent_goal]]
    main_problem.distances = {}
    for vertex in main_problem.graph:
        main_problem.distances[vertex] = dijkstra_distance(main_problem.graph, vertex)
    paths, cost = MAXSATSolver(main_problem).solve()
    reverse_paths = [[] for _ in range(main_problem.n_agents)]
    for t in paths:
        for a, v in enumerate(t):
            reverse_paths[a].append((v % len(problem.grid), divmod(v, len(problem.grid))[0]))
    print(paths, cost)
    return Solution.from_paths(reverse_paths)


if __name__ == '__main__':
    benchmarker = MapfBenchmarker("5gxwhXLoYfS8AwrK", 133, "MaxSAT",
                                  "Without + 2", False, solver=solverMaxSAT, cores=1)
    benchmarker.run()
