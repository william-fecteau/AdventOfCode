from math import prod
from utils.aoc_utils import AOCDay
import numpy as np
import re


class Day3(AOCDay):
    def common(self):
        m, n = len(self.inputData), len(self.inputData[0])
        self.grid = np.zeros((m, n), dtype='int')

        for i, line in enumerate(self.inputData):
            for num_match in re.finditer(r'\d+', line):
                start, end = num_match.span()
                self.grid[i, start:end] = int(line[start:end])

    def find_adjacent_engine_ids(self, i, j):
        m, n = self.grid.shape
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0),
                     (1, -1), (-1, -1), (1, 1), (-1, 1)]

        engine_ids = set()
        for dx, dy in neighbors:
            k, l = i + dx, j + dy
            if 0 <= k < m and 0 <= l < n and self.grid[k, l] != 0:
                engine_ids.add(self.grid[k, l])

        return engine_ids

    def part1(self):
        engine_id_sum = 0
        for i, line in enumerate(self.inputData):
            for operator_match in re.finditer(r'[^\d.]', line):
                j = operator_match.start()

                engine_id_sum += sum(self.find_adjacent_engine_ids(i, j))

        return engine_id_sum

    def part2(self):
        gear_ratio_sum = 0
        for i, line in enumerate(self.inputData):
            for star_match in re.finditer(r'\*', line):
                j = star_match.start()

                engine_ids = self.find_adjacent_engine_ids(i, j)
                if len(engine_ids) == 2:
                    gear_ratio_sum += prod(engine_ids)

        return gear_ratio_sum
