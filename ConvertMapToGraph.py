from utils import convert_grid_dict_ints

grid = []
with open('room32.map') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        grid.append([])
        for value in line:
            if value == ".":
                grid[i].append(0)
            else:
                grid[i].append(1)

graph = convert_grid_dict_ints(grid)
file = "type graph\n"
file += "nodes " + str(len(graph)) + "\n"
file += "map\n"

for key in graph:
    file += str(key) + " " + ' '.join([str(v) for v in graph[key]]) + "\n"
f = open("waypointsR_3.graph", "w")
print(f.write(file))