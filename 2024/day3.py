import re

import numpy as np
from utils.aoc_utils import AOCDay

class Day3(AOCDay):
    def common(self):
        self.mulRegex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    def part1(self):
        return sum([int(left)*int(right) for left, right in re.findall(self.mulRegex, self.rawData)])

    def part2(self):
        dos = np.array([match.start() for match in re.finditer(r"do\(\)", self.rawData)])
        dont = np.array([match.start() for match in re.finditer(r"don't\(\)", self.rawData)])

        sum = 0
        for match in re.finditer(self.mulRegex, self.rawData):
            dos_diff = dos - match.start()
            dont_diff = dont - match.start()

            dos_diff = dos_diff[dos_diff < 0]
            dont_diff = dont_diff[dont_diff < 0]

            closest_do = np.max(dos_diff) if len(dos_diff) > 0 else -9999
            closest_dont = np.max(dont_diff) if len(dont_diff) > 0 else -9999

            if closest_do >= closest_dont:
                left, right = match.groups()
                sum += int(left) * int(right)

        return sum
