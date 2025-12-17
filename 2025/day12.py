import numpy as np
from utils.aoc_utils import AOCDay
from scipy.spatial.transform import Rotation

class Day12(AOCDay):
    def common(self):
        groups = []
        current = []
        for line in self.inputData:
            if line != "":
                current.append(line)
            else:
                groups.append(current)
                current = []
        
        groups.append(current)

        # Extracting shapes
        self.shapes = []
        for group in groups[:-1]:
            matrix = []
            for line in group[1:]:
                matrix.append(list(map(int, list(line.replace("#", "1").replace(".", "0")))))

            self.shapes.append(matrix)
        self.shapes = np.array(self.shapes)
        
        # Extracting regions
        self.regions = []
        for line in groups[-1]:
            splitted = line.split(":")

            n, m = splitted[0].split("x")
            n = int(n); m = int(m)

            quantities = list(map(int, list(splitted[1][1:].split(" "))))
        

            self.regions.append({
                "shape": (n, m),
                "quantities": np.array(quantities)
            })

    def part1(self):
        count = 0
        shape_coverage = np.array([np.sum(shape) for shape in self.shapes])
        for region in self.regions:
            region_total_tiles = region["shape"][0] * region["shape"][1]

            if sum(np.multiply(shape_coverage, region["quantities"])) <= region_total_tiles:
                count += 1 

        return count

    def part2(self):
        return 0
