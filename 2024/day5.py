from itertools import permutations
from utils.aoc_utils import AOCDay
import networkx	as nx

class Day5(AOCDay):
    def common(self):
        self.rules = {}
        split_idx = 0
        for i, line in enumerate(self.inputData):
            if line == "":
                split_idx = i
                break
                
            left, right = line.split("|")
            left = int(left); right = int(right)
            if not left in self.rules:
                self.rules[left] = []

            self.rules[left].append(right)
        
        self.updates = []
        for line in self.inputData[split_idx+1:]:
            self.updates.append([int(x) for x in line.split(",")])


    def is_rule_respected(self, left, right, update):
        try:
            left_i = update.index(left)
            right_i = update.index(right)
        except ValueError:
            return True
        
        return left_i < right_i


    def is_update_correct(self, update):
        is_valid = True
        violated_rules = []
        for left in self.rules.keys():
            if not left in update:
                continue

            for right in self.rules[left]:
                if not self.is_rule_respected(left, right, update):
                    is_valid = False
                    violated_rules.append((left, right))
        
        return is_valid, violated_rules


    def part1(self):
        correct_updates = []
        self.incorrect_updates = []
        for update in self.updates:
            is_correct, violated_rules = self.is_update_correct(update)
            if is_correct:
                correct_updates.append(update)
            else:
                self.incorrect_updates.append((update, violated_rules))

        
        return sum([x[len(x)//2] for x in correct_updates])


    def part2(self):
        correct_updates = []
        for update, violated_rules in self.incorrect_updates:
            print(violated_rules)
        
        return sum([x[len(x)//2] for x in correct_updates])



