import numpy as np
from utils.aoc_utils import AOCDay

class Day4(AOCDay):
    def common(self):
        word_search = []
        for line in self.inputData:
            word_search.append([char for char in line])
        
        self.word_search = np.array(word_search)

    def part1(self):
        n = self.word_search.shape[0]

        horizontals = ["".join(line) for line in self.word_search]
        verticals = ["".join(line) for line in self.word_search.T]
        diagonals_1 = ["".join(self.word_search.diagonal(i)) for i in range(-n+1, n)]
        diagonals_2 = ["".join(np.fliplr(self.word_search).diagonal(i)) for i in range(-n+1, n)]
        
        count = 0
        for direction in [horizontals, verticals, diagonals_1, diagonals_2]:
            for line in direction:
                count += line.count("XMAS") + line.count("SAMX")
               
        return count

    def part2(self):
        n = self.word_search.shape[0]

        count = 0
        for i in range(1, n-1):
            for j in range(1, n-1):
                if self.word_search[i, j] != "A":
                    continue

                diag_1 = self.word_search[i+1, j+1] + "A" + self.word_search[i-1, j-1]
                diag_2 = self.word_search[i+1, j-1] + "A" + self.word_search[i-1, j+1]

                if (diag_1 == "MAS" or diag_1 == "SAM") and (diag_2 == "MAS" or diag_2 == "SAM"):
                    count += 1

        return count
