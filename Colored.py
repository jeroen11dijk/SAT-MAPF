import itertools

from MAXSATSolverColored import MAXSATSolverColored
from Problem_generator import safe_generate_grid
from mstar import Mstar
from problem_classes import ColoredProblem
from utils import convert_grid_dict_ints, dijkstra_distance

if __name__ == '__main__':
    grid = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    starts = [[0, 8], [2]]
    goals = [[6, 4], [3]]
    graph = convert_grid_dict_ints(grid)
    distances = {}
    for vertex in graph:
        distances[vertex] = dijkstra_distance(graph, vertex)
    options = {}
    makespans = []
    heuristics = []
    for team in zip(starts, goals):
        for start in team[0]:
            options[start] = team[1]
        opt = float('inf')
        makespan = float('inf')
        for matching in [list(zip(perm, team[1])) for perm in itertools.permutations(team[0], len(team[1]))]:
            heuristic = []
            for match in matching:
                heuristic.append(distances[match[1]][match[0]])
            if sum(heuristic) < opt:
                opt = sum(heuristic)
                makespan = max(heuristic)
        makespans.append(makespan)
        heuristics.append(opt)
    starts = [item for sublist in starts for item in sublist]
    res, cost = MAXSATSolverColored(ColoredProblem(3, graph, starts, options, distances, heuristics, max(makespans))).solve()
    print(res, cost)
    print(Mstar(graph, tuple([0, 5, 8]), ((), (), (), (), (), (), (), (), (), ()),
          tuple([6, 4, 3]), {}).solve())
    print(Mstar(graph, tuple([0, 5, 8]), ((), (), (), (), (), (), (), (), (), ()),
          tuple([4, 6, 3]), {}).solve())