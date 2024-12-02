import math
from utils.aoc_utils import AOCDay
import re


class Day6(AOCDay):
    def common(self):
        self.times = [int(x) for x in re.findall(r'\d+', self.inputData[0])]
        self.distances = [int(x)
                          for x in re.findall(r'\d+', self.inputData[1])]

    def solve_2nd_degree(self, a, b, c):
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return None
        elif delta == 0:
            return -b / (2 * a)
        else:
            return (-b - delta ** 0.5) / (2 * a), (-b + delta ** 0.5) / (2 * a)

    def solve_nb_ways_to_win(self, t, d):
        t1, t2 = self.solve_2nd_degree(-1, t, -d)

        t1, t2 = (t1, t2) if t1 < t2 else (t2, t1)

        t1 = math.floor(t1)
        t2 = math.floor(t2)

        # Exclusive bound
        if (t2 * (t - t2) <= d):
            t2 -= 1

        return t2 - t1

    def part1(self):
        return math.prod([self.solve_nb_ways_to_win(t, d) for t, d in zip(self.times, self.distances)])

    def part2(self):
        t = int(self.inputData[0].replace(' ', '').split(':')[1])
        d = int(self.inputData[1].replace(' ', '').split(':')[1])

        return self.solve_nb_ways_to_win(t, d)
