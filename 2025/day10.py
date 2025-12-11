import numpy as np
from utils.aoc_utils import AOCDay
from pulp import LpProblem, LpVariable, lpSum, LpInteger, LpMinimize, LpStatus, value


class Day10(AOCDay):
    def common(self):
        self.goals = []
        self.button_indexes = []
        self.all_buttons = []
        self.all_joltages = []
        for line in self.inputData:
            splitted = line.split(" ")
            str_goal = splitted[0][1:-1].replace(".", "0").replace("#", "1")
            goal = int(str_goal, 2)

            buttons = []
            button_indexes = []
            buttons_str = splitted[1:-1]
            for button_str in buttons_str:
                ones_pos = np.array(eval(button_str[1:-1]))
                bits = np.zeros(len(str_goal), dtype=np.uint8)
                bits[ones_pos] = 1
                button = int("".join(map(str, bits)), 2)

                button_indexes.append(ones_pos)
                buttons.append(button)
            
            joltages = np.array(eval(splitted[-1][1:-1]))

            self.goals.append(goal)
            self.button_indexes.append(button_indexes)
            self.all_buttons.append(buttons)
            self.all_joltages.append(joltages)

    def part1(self):
        button_presses = []
        for goal, buttons in zip(self.goals, self.all_buttons):
            start = 0
            
            accesible_states = {start}
            count = 0
            while goal not in accesible_states:
                accesible_states = {state ^ button for state in accesible_states for button in buttons}
                count += 1
            
            button_presses.append(count)

        return sum(button_presses)

    def part2(self):
        button_presses = []
        for joltages, button_indexes in zip(self.all_joltages, self.button_indexes):
            # Build A matrix
            A = []
            for i in range(len(joltages)):
                line = [int(i in indexes) for indexes in button_indexes]
                A.append(line)
            
            A = np.array(A)
            b = np.array(joltages)
            
            n_vars = A.shape[1]
            
            # ILP formulation
            prob = LpProblem("ButtonPresses", LpMinimize)
            
            # Decision variables
            x = [LpVariable(f"x{i}", cat=LpInteger, lowBound=0) for i in range(n_vars)]
            
            # Objective
            prob += lpSum(x)
            
            # Constraints A x = b
            for i in range(A.shape[0]):
                prob += lpSum(A[i,j] * x[j] for j in range(n_vars)) == b[i]
            
            prob.solve()
            
            nb_presses = sum([int(value(var)) for var in x])
            button_presses.append(nb_presses)

        return sum(button_presses)
