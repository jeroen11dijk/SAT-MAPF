from heapq import heappush, heappop


def convert_graph(graph):
    grap_new = {}
    height = len(graph)
    width = len(graph[0])
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                current = width * i + j
                neighbours = []
                if i != 0 and graph[i - 1][j] == 0:
                    neighbours.append(width * (i - 1) + j)
                if j != 0 and graph[i][j - 1] == 0:
                    neighbours.append(width * i + j - 1)
                if i != height - 1 and graph[i + 1][j] == 0:
                    neighbours.append(width * (i + 1) + j)
                if j != width - 1 and graph[i][j + 1] == 0:
                    neighbours.append(width * i + j + 1)
                grap_new[current] = neighbours
    return grap_new


def euclidian_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dijkstra_predecessor_and_distance(G, source):
    dist = {}  # dictionary of final distances
    pred = {source: []}  # dictionary of predecessors
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
                pred[neighbour] = [v]
            elif vw_dist == seen[neighbour]:
                pred[neighbour].append(v)
    return pred, dist


def dijkstra_distance(G, source):
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
