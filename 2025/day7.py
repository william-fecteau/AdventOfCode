import numpy as np
from utils.aoc_utils import AOCDay

class Day7(AOCDay):
    def common(self):
        self.matrix = np.array([list(line) for line in self.inputData])

    def part1(self):
        split_count = 0
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                char = self.matrix[i, j]

                if char == "S":
                    self.matrix[i+1, j] = "|"
                elif char == "^" and self.matrix[i-1, j] == "|":
                    self.matrix[i, j+1] = "|"
                    self.matrix[i, j-1] = "|"
                    split_count += 1
                elif char == "." and self.matrix[i-1, j] == "|":
                    self.matrix[i, j] = "|"

        return split_count
                 
    def part2(self):
        timelines_per_beam = [0] * self.matrix.shape[1]
        
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                char = self.matrix[i, j]

                if char == "S":
                    self.matrix[i+1, j] = "|"
                    timelines_per_beam[j] = 1
                elif char == "^" and self.matrix[i-1, j] == "|":
                    self.matrix[i, j-1] = "|"
                    self.matrix[i, j+1] = "|"
                    
                    timelines_per_beam[j-1] += timelines_per_beam[j]
                    timelines_per_beam[j+1] += timelines_per_beam[j]
                    timelines_per_beam[j] = 0
                elif char == "." and self.matrix[i-1, j] == "|":
                    self.matrix[i, j] = "|"

        return sum(timelines_per_beam)


