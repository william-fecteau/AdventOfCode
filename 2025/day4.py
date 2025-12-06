import numpy as np
from scipy.signal import convolve2d
from utils.aoc_utils import AOCDay

class Day4(AOCDay):
    def common(self):
        self.matrix = []
        for line in self.inputData:
            temp = line.replace(".", "0").replace("@", "1")
            line_arr = [int(c) for c in temp]
            self.matrix.append(line_arr)
        
        self.matrix = np.array(self.matrix)

    def apply_convolution(self):
        kernel = np.ones((3,3), dtype=int)
        kernel[1, 1] = 0

        result = convolve2d(self.matrix, kernel, mode="same")
        sub_4_result = np.where((result < 4) & (self.matrix == 1), 1, 0)

        return sub_4_result

    def part1(self):
        return np.sum(self.apply_convolution())

    def part2(self):
        cur_sum = 69
        total_sum = 0
        while cur_sum > 0:
            result = self.apply_convolution()
            self.matrix = np.logical_xor(self.matrix, result).astype(int)

            cur_sum = np.sum(result)
            total_sum += cur_sum

        return total_sum


            
    
