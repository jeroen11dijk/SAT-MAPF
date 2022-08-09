import random

import numpy

from utils import convert_grid_dict_ints
import string

class Node:
    def __init__(self, name : string , neighbors : list):
        self.name = name
        self.neighbors = neighbors

    def add_neighbor(self, name : string):
        if(self.neighbors.count(name) == 0):
            self.neighbors.append(name)

    def remove_neighbor(self, name : string):
        assert(self.neighbors.count(name) == 0)
        self.neighbors.remove(name)

    def degree(self) -> int:
        return self.neighbors.__len__()

    def to_string(self) -> string:
        return self.name

    def rename(self, new_name : string):
        self.name = new_name

    def in_branch(self, branch : int)-> bool:
        if self.name[0] == "g":
            return True
        if self.name[0] == "root":
            return False
        if self.name[0] != "b":
            raise Exception("Node not in gate nor in branch nor gate")
        b1 = int(self.name.split("-")[1])
        return b1 == branch

    def dist_to_root(self) -> int:
        if self.name[0] == "g":
            raise Exception("dist to root not implemented for gate nodes")
        if self.name[0] == "root":
            return 0
        if self.name[0] != "b":
            raise Exception("Node not in gate nor in branch nor gate")
        return int(self.name.split("-")[3])

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Agent:
    def __init__(self, name : string, type: string, start : Node, goal : Node, waypoints):
        self.name = name
        if type == None:
            self.type = name
        else:
            self.type = type
        self.start = start
        self.goal = goal
        self.waypoints = waypoints

    def match(self, num_of_types : int):
        self.type = str( int(self.name) % num_of_types )

    def to_string(self) -> string:
        return self.name

def get_types(agents) -> list:
    types = []
    for agent in agents:
        if types.count(agent.type) == 0:
            types.append(agent.type)
    return types

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
print(grid)
path = "waypointsR_3"
min_agents = 4
max_agents = 100
num_of_instances_per_num_agents = 10
num_of_types = 0
n_waypoints = 3
for aa in range(min_agents,max_agents+1):
    for ii in range(num_of_instances_per_num_agents):
        num_of_agents = aa
        graph = convert_grid_dict_ints(grid)
        agents = []
        nodes = list(graph.keys())
        starts = set()
        goals = set()
        for number in range(num_of_agents):
            start = random.choice(nodes)
            while start in starts:
                start = random.choice(nodes)
            starts.add(start)
            goal = random.choice(nodes)
            while goal in goals:
                goal = random.choice(nodes)
            goals.add(goal)
            waypoints = []
            while len(waypoints) < n_waypoints:
                waypoint = random.choice(nodes)
                while waypoint in waypoints:
                    waypoint = random.choice(nodes)
                waypoints.append(waypoint)
            new_agent = Agent(str(number), None, start, goal, waypoints)
            agents.append(new_agent)
        print(agents)
        if num_of_types != 0:
            for agent in numpy.random.permutation(agents):
                agent.match(num_of_types)
        file_name = str(aa) + "a_" + str(ii) + ".scen"
        first_lines = "version 1 graph" + "\n"
        first_lines += "waypointsR_3.graph" + "\n"
        first_lines += "Num_of_Agents " + str(agents.__len__()) + "\n"
        body = "types" + "\n"
        for type in get_types(agents):
            body += type
            for agent in agents:
                if agent.type == type:
                    body += " " + agent.to_string()
            body += "\n"
        body += "agents starts" + "\n"
        for agent in agents:
            body += agent.to_string() + " " + str(agent.start) + "\n"
        body += "goals" + "\n"
        for agent in agents:
            body += agent.to_string() + " " + str(agent.goal) + "\n"
        body += "waypoints"
        for agent in agents:
            body += "\n" + agent.to_string() + " " + ' '.join(map(str, agent.waypoints))
        f = open(path + "/" + file_name, 'w')
        f.write(first_lines + body)
        f.close()
