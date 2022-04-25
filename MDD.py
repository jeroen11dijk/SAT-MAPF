from collections import defaultdict
from collections import deque
from heapq import heappush, heappop


def dijkstra_predecessor_and_distance(G, source):
    dist = {}  # dictionary of final distances
    seen = {source: 0}
    c = 1
    fringe = []  # use heapq with (distance,label) tuples
    heappush(fringe, (0, c, source))
    while fringe:
        (d, _, v) = heappop(fringe)
        if v in dist:
            continue  # already searched this node.
        dist[v] = d
        neighbours = G[v]
        for neighbour in neighbours:
            vw_dist = d + 1
            if neighbour not in seen or vw_dist < seen[neighbour]:
                seen[neighbour] = vw_dist
                c += 1
                heappush(fringe, (vw_dist, c, neighbour))
    return dist


def generate_MDD(graph, start, goal, depth, distances):
    res = set()
    for vertex in graph:
        if distances[vertex][start] + distances[goal][vertex] <= depth:
            res.add(vertex)
    return res


class MDD:
    def __init__(self, my_map, agent, start, goal, depth, generate=True, last_mdd=None):
        """ Note that in order to save memory, we do not store the map on each
        MDD, but instead pass the map as an argument to the generation function"""
        self.agent = agent
        self.start = start
        self.goal = goal
        self.depth = depth
        self.mdd = None
        self.level = defaultdict(set)
        self.bfs_tree = {}
        if generate:
            if last_mdd and last_mdd.depth < depth and last_mdd.agent == agent:
                self.generate_mdd(my_map, last_mdd)
            else:
                self.generate_mdd(my_map)

    def generate_mdd(self, my_map, last_mdd=None):
        if last_mdd:
            bfs_tree = self.bootstrap_depth_d_bfs_tree(my_map, self.start, self.depth, last_mdd.bfs_tree)
        else:
            bfs_tree = self.get_depth_d_bfs_tree(my_map, self.start, self.depth)
        self.bfs_tree = bfs_tree
        mdd = self.bfs_to_mdd(bfs_tree['tree'], self.start, self.goal, self.depth)
        self.mdd = mdd
        if mdd:
            self.populate_levels(self.mdd)

    def populate_levels(self, mdd):
        self.level[0] = {self.start}
        for adjacent in mdd.values():
            for node in adjacent:
                self.level[node[1]].add(node[0])

    def get_depth_d_bfs_tree(self, my_map, start, depth):
        # Run BFS to depth 'depth' to find the solutions for this agent
        fringe = deque()
        fringe.append((start, 0))
        prev_dict = defaultdict(set)
        visited = set()
        bfs_tree = self.main_bfs_loop(my_map, start, depth, fringe, prev_dict, visited)
        return bfs_tree

    def bootstrap_depth_d_bfs_tree(self, my_map, start, depth, old_tree):
        fringe = deque()
        old_fringe = list(old_tree['fringe'])
        old_fringe.sort(key=lambda x: x[0][0] + x[0][1])
        fringe.extend(old_fringe)
        prev_dict = old_tree['tree']
        for node in old_fringe:
            node_prevs = old_tree['fringe_prevs'][node]
            prev_dict[node].update(node_prevs)
        visited = old_tree['visited']
        new_bfs_tree = self.main_bfs_loop(my_map, start, depth, fringe, prev_dict, visited)
        return new_bfs_tree

    def main_bfs_loop(self, my_map, start, depth, fringe, prev_dict, visited):
        depth_d_plus_one_fringe = set()
        fringe_prevs = defaultdict(set)
        while fringe:
            curr = fringe.popleft()
            loc, d = curr
            children = self.get_valid_children(my_map, loc, d)
            for c in children:
                if c[1] <= depth:
                    prev_dict[c].add(curr)
                    if c not in visited:
                        fringe.append(c)
                        visited.add(c)
                if c[1] == depth + 1:
                    depth_d_plus_one_fringe.add(c)
                    fringe_prevs[c].add(curr)
        return {'tree': prev_dict, 'visited': visited, 'depth': depth, 'fringe': depth_d_plus_one_fringe,
                'fringe_prevs': fringe_prevs}

    def bfs_to_mdd(self, bfs_tree, start, goal, depth):
        # Convert a complete bfs tree to an mdd
        goal_time = (goal, depth)
        visited = set()
        if not bfs_tree[goal_time]:
            return None
        mdd = defaultdict(set)
        trace_list = deque()
        for parent in bfs_tree[goal_time]:
            trace_list.append((parent, goal_time))
            visited.add((parent, goal_time))
        while trace_list:
            curr, child = trace_list.popleft()
            mdd[curr].add(child)
            for p in bfs_tree[curr]:
                if (p, curr) not in visited:
                    visited.add((p, curr))
                    trace_list.append((p, curr))
        return mdd

    def get_valid_children(self, my_map, loc, d):
        # Get all children that are on the map
        good_children = [(loc, d + 1)]
        for c in my_map[loc]:
            good_children.append((c, d + 1))
        return good_children


if __name__ == '__main__':
    graph = {0: [4, 1], 1: [0, 5, 2], 2: [1, 6, 3], 3: [2, 7], 4: [0, 8, 5], 5: [1, 4, 9, 6], 6: [2, 5, 10, 7],
             7: [3, 6, 11], 8: [4, 12, 9], 9: [5, 8, 13, 10], 10: [6, 9, 14, 11], 11: [7, 10, 15], 12: [8, 13],
             13: [9, 12, 14], 14: [10, 13, 15], 15: [11, 14]}
    edges = set()
    for v in graph:
        edges.add((v, v))
    for key in graph:
        for value in graph[key]:
            edges.add((key, value))
    distances = {}
    for vertex in graph:
        distances[vertex] = dijkstra_predecessor_and_distance(graph, vertex)
    print(generate_MDD(graph, 0, 9, 6, distances))
    mdd = MDD(graph, 0, 0, 1, 2)
    print(mdd.bfs_tree)
    print(mdd.mdd)
