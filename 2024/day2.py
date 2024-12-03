import numpy as np
from utils.aoc_utils import AOCDay

class Day2(AOCDay):
    def common(self):
        self.reports = []
        for line in self.inputData:
            levels = list(map(lambda x: int(x), line.split(" ")))

            self.reports.append(levels)

    def is_diff_safe(self, diff):
        return all(x >= 1 and x <=3 for x in diff) or all(x <= -1 and x >= -3 for x in diff)

    def part1(self):
        safe_count = 0
        for report in self.reports:
            diff = np.diff(report)
            if self.is_diff_safe(diff):
                safe_count += 1
        
        return safe_count


    def part2(self):
        safe_count = 0
        for report in self.reports:
            for i in range(len(report)):
                diff = np.diff(report[:i] + report[i+1:])
                if self.is_diff_safe(diff):
                    safe_count += 1
                    break

        return safe_count
