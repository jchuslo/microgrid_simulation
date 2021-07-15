import numpy as np
import pandas as pd
import os

import networkx as nx

# each unit has a panel w/ an efficiency and a battery

# create communication network in a complete graph

# create a dc (one way) grid

# create discrete time


class HousingUnit():

    def __init__(self):
        
        self.solar_efficiency = 0.2 # 20%
        self.battery_capacity = 3 # 3 units

    def talk(other_unit):
        pass


class Grid():

    def __init__(self, nodes: list):

        self.time = 0
        
        self.edge_list = [(a, b) for a in nodes for b in nodes[nodes.index(a)+1:]]
        
        self.net = nx.Graph()
        for (a, b) in self.edge_list:
            self.net.add_edge(a, b)

        self.dc_loc = 0

    def time_step(self):

        # do stuff here to trade electricity
        ###

        if self.dc_loc == (len(self.edge_list) - 1):
            self.dc_loc = 0
        else:
            self.dc_loc += 1

        
        self.time += 1
        print("time step happened.")

    def simulate(self, num_steps):

        while self.time < num_steps:
            self.time_step()




# Main code

house1 = HousingUnit()
house2 = HousingUnit()
house3 = HousingUnit()

network = Grid([house1, house2, house3])

network.simulate(10)
