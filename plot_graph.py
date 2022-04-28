import networkx as nx
import pylab

if __name__ == '__main__':
    if True:
        graph = {}
        for line in open('carrousel_random_25n_5b_5g_0.0r.graph').readlines()[3:]:
            # graph[convert[line.split()[0]]] = [convert[node] for node in line.split()[1:]]
            graph[line.split()[0]] = line.split()[1:]
    else:
        problem = safe_generate_grid(8, 1, 8, 0.1)
        graph = convert_graph(problem.grid)
    G = nx.DiGraph(graph)
    nx.draw(G, pos=nx.spring_layout(G, k=0.2, iterations=20))
    pylab.show()
