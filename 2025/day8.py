import numpy as np
from utils.aoc_utils import AOCDay
from scipy.spatial import distance_matrix
import networkx as nx

class Day8(AOCDay):
    def common(self):
        self.points = []
        for line in self.inputData:
            data = line.split(",")

            self.points.append([int(data[0]), int(data[1]), int(data[2])])

        D = distance_matrix(self.points, self.points)
        self.G = nx.Graph()
        
        # Ignore the lower triangle (Euclidian distance = symetric matrix)
        self.upper_dists = np.triu(D, k=1)
        self.upper_dists[self.upper_dists == 0] = 696969
        
    def make_connection(self):
        idx = np.argmin(self.upper_dists)
        i, j = np.unravel_index(idx, self.upper_dists.shape)

        self.G.add_edge(i, j)

        self.upper_dists[i, j] = 696969

        return i, j

    def part1(self):
        for _ in range(1000):
            self.make_connection()
        
        connections = list(nx.connected_components(self.G))
        nb_junctions = [len(x) for x in connections]
        nb_junctions.sort()

        return np.prod(nb_junctions[-3:])

    def part2(self):
        while len(list(nx.connected_components(self.G))) > 1:
            last_connection = self.make_connection()
        
        point_a = self.points[last_connection[0]]
        point_b = self.points[last_connection[1]]

        return point_a[0] * point_b[0]
        

