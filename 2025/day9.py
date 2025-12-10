import shapely
from utils.aoc_utils import AOCDay
import matplotlib.pyplot as plt

class Day9(AOCDay):
    def common(self):
        self.points = []
        for line in self.inputData:
            data = line.split(",")

            self.points.append([int(data[0]), int(data[1])])

    def part1(self):
        areas = []
        for a in self.points:
            for b in self.points:
                dx = abs(a[0] - b[0])+1
                dy = abs(a[1] - b[1])+1

                areas.append(dx*dy)                
        
        return max(areas)

    def part2(self):
        poly = shapely.Polygon(self.points)

        areas = []
        for a in self.points:
            for b in self.points:
                subpoly = shapely.Polygon([a, [a[0], b[1]], b, [b[0], a[1]]])
                
                if poly.covers(subpoly):
                    dx = abs(a[0] - b[0])+1
                    dy = abs(a[1] - b[1])+1

                    areas.append(dx*dy)

                # areas.append()

        return max(areas)
