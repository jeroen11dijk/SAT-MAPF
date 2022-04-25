import random
from dataclasses import dataclass
from typing import Tuple, Set, FrozenSet


@dataclass
class MMAPFW:
    def __init__(self, grid, n_teams, n_agents, starts, goals, waypoints):
        self.grid = grid
        self.n_teams = n_teams
        self.n_agents = n_agents
        self.starts = starts
        self.goals = goals
        self.waypoints = waypoints


def neighbours(tiles: Set[Tuple[int, int]],
               tile: Tuple[int, int]) -> Set[Tuple[int, int]]:
    neighbours = set()
    for xOffs in [-1, 0, 1]:
        for yOffs in [-1, 0, 1]:
            if not (xOffs == 0 or yOffs == 0):
                continue

            neighbour = tile[0] + xOffs, tile[1] + yOffs

            if neighbour not in tiles:
                continue

            neighbours.add(neighbour)

    return neighbours


def group_of(tiles: Set[Tuple[int, int]],
             tile: Tuple[int, int]) -> Set[Tuple[int, int]]:
    visited = set()

    queue = [tile]
    while len(queue) > 0:
        visiting = queue.pop()
        if visiting in visited:
            continue
        visited.add(visiting)
        queue.extend(neighbours(tiles, visiting))

    return visited


def find_groups(tiles: Set[Tuple[int, int]]) -> \
        Set[FrozenSet[Tuple[int, int]]]:
    unvisited = tiles.copy()

    groups = set()

    while len(unvisited) > 0:
        tile = next(iter(unvisited))
        group = group_of(unvisited, tile)
        unvisited -= group
        groups.add(frozenset(group))

    return groups


def find_disconnected(tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    groups = find_groups(tiles)
    groups.remove(max(groups, key=lambda g: len(g)))

    disconnected = set()
    for group in groups:
        for tile in group:
            disconnected.add(tile)

    return disconnected


def generate_grid(teams: int, agents: int, size: int, infill: float) -> MMAPFW:
    grid = [[0] * size for _ in range(size)]
    tiles = [(x, y) for y in range(size) for x in range(size)]
    # 20% walls
    for _ in range(int(size * size * infill)):
        tile = random.choice(tiles)
        tiles.remove(tile)
        x, y = tile
        grid[y][x] = 1

    # Remove disconnected sections
    for tile in find_disconnected(set(tiles)):
        tiles.remove(tile)
        x, y = tile
        grid[y][x] = 1

    # Agents
    starts = []
    goals = []
    agent_waypoints = [frozenset() for _ in range(agents * teams)]
    for team in range(teams):
        team_starts = []
        team_goals = []
        for agent in range(agents):
            # Waypoints
            temp = set()
            for _ in range(random.choice([0, 1])):
                waypoint = random.choice(tiles)
                tiles.remove(waypoint)
                temp.add(waypoint)
            agent_waypoints[team * agent + agent] = frozenset(temp)
            start = random.choice(tiles)
            tiles.remove(start)
            goal = random.choice(tiles)
            tiles.remove(goal)
            team_starts += [start]
            team_goals += [goal]
        starts.append(team_starts)
        goals.append(team_goals)

    return MMAPFW(grid=grid, n_teams=teams, n_agents=agents * teams, starts=starts, goals=goals,
                  waypoints=agent_waypoints)


def safe_generate_grid(teams: int, agents: int, size: int,
                       infill: float = 0.2) -> MMAPFW:
    problem = None
    while problem is None:
        try:
            problem = generate_grid(teams, agents, size, infill)
        except IndexError:
            problem = None
    return problem
