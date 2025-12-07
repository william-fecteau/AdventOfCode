import numpy as np
from utils.aoc_utils import AOCDay

class Day6(AOCDay):
    def common(self):
        self.char_matrix = np.array([[c for c in line] for line in self.inputData[:-1]])

        # Separators
        self.separators = []
        for i in range(self.char_matrix.shape[1]):
            if np.all(self.char_matrix[:, i] == " "):
                self.separators.append(i)
        self.separators.append(self.char_matrix.shape[1])
        
        # Numbers
        self.all_numbers = []
        for line in self.inputData[:-1]:
            next_start = 0
            numbers = []
            for separator in self.separators:
                numbers.append(int(line[next_start:separator]))
                next_start = separator+1
            
            self.all_numbers.append(numbers)

        self.all_numbers = np.array(self.all_numbers)
        
        # Operators
        self.operators = []
        operator_line = self.inputData[-1]
        next_start = 0
        for separator in self.separators:
            operator = operator_line[next_start:separator].strip()
            self.operators.append(operator)
            next_start = separator+1

        self.operators = np.array(self.operators)

    def part1(self):
        final_sum = 0
        for i, operator in enumerate(self.operators):
            if operator == "+":
                final_sum += np.sum(self.all_numbers[:, i]) # type: ignore
            elif operator == "*":
                final_sum += np.prod(self.all_numbers[:, i]) # type: ignore

        return final_sum

    def part2(self):
        cols = []
        next_start = 0
        for separator in self.separators:
            col = []
            for i in range(next_start, separator):
                current_num = int("".join(self.char_matrix[:, i]))
                col.append(current_num)
                next_start = separator+1

            cols.append(col)
        
        final_sum = 0
        for i, operator in enumerate(self.operators):
            if operator == "+":
                final_sum += np.sum(cols[i])
            if operator == "*":
                final_sum += np.prod(cols[i])

        return final_sum
