import matplotlib.pyplot as plt
import math

names = {1: "SAT Solver", 2: "MaxSAT Solver", 3: "Inflated MaxSAT Solver", 4: "M*", 5:"Prematch SAT", 6: "Prematch MaxSAT"}
graph_names = ["8x8 grid, 3 teams", "32x32 grid, 3 teams", "8x8 grid, 1 team", "32x32 grid, 1 team", "carrousel graph, 3 teams", "carrousel graph, 1 team", "rooms, 3 teams", "rooms, 1 team"]
for graph_index, file_base in enumerate(["grid8_", "grid32_", "grid8_1_", "grid32_1_", "carrousel_3_", "carrousel_1_", "room32_", "room32_1_"]):
    costs = {}
    res = []
    if "room" in file_base:
        up = 5
    else:
        up = 7
    for i in range(1, up):
        print(file_base)
        lines = open("results_colored/" + file_base + str(i) + ".txt").read().splitlines()
        costs_i = {}
        res_i = {}
        for index in range(0, len(lines), 2):
            file = lines[index].split(".")[0]
            agents = file.split("a")[0]
            costs_i[file] = int(lines[index+1])
            if agents not in res_i:
                res_i[agents] = 1
            else:
                res_i[agents] += 1
        costs[i] = costs_i
        plt.plot(list(res_i.values()) + [0], label=names[i])
    plt.legend()
    plt.locator_params(axis="both", integer=True, tight=True)
    plt.xlabel("Number of agents")
    plt.ylabel("Instances solved")
    plt.title(graph_names[graph_index])
    plt.savefig(graph_names[graph_index] + ".png",bbox_inches='tight')
    plt.clf()
    # plt.show()
    opt_costs = costs[1]
    maxsat = []
    inflated = []
    for key in costs[2].keys():
        if key in opt_costs:
            maxsat.append(((costs[2][key] - opt_costs[key]) / opt_costs[key]) * 100.0)
    for key in costs[3].keys():
        if key in opt_costs:
            inflated.append(((costs[3][key] - opt_costs[key]) / opt_costs[key]) * 100.0)
    print(graph_names[graph_index])
    print((maxsat.count(0) / len(maxsat)) * 100)
    print((inflated.count(0) / len(inflated)) * 100)
