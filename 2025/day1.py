import numpy as np
from utils.aoc_utils import AOCDay

class Day1(AOCDay):
    def common(self):
        self.dial_max = 100
        current_dial = 50

        self.steps = [current_dial]
        self.rotations = []

        for line in self.inputData:
            direction = line[0]
            ticks = int(line[1:])

            side = 1 if direction == "R" else -1
            rotation = side * ticks
            self.rotations.append(rotation)

            current_dial += rotation
            self.steps.append(current_dial % self.dial_max)
        
        self.rotations = np.array(self.rotations)
        self.steps = np.array(self.steps) 

    def part1(self):
        self.zero_indexes = np.where(self.steps == 0)[0]
        return len(self.zero_indexes)
        
    def part2(self):
        count = 0
        for current_dial, dial_after, rotation in zip(self.steps[:-1], self.steps[1:], self.rotations):
            # Full rotation
            count += abs(rotation) // self.dial_max

            # Dial lands on zero
            count += int(dial_after == 0)

            # No crossing if its already 0
            if current_dial == 0:
                continue

            # Check if it crosses zero for the rest
            rotation_rest = abs(rotation) % self.dial_max
            if rotation < 0 and rotation_rest > current_dial:
                count += 1
            elif rotation > 0 and rotation_rest > self.dial_max - current_dial:
                count += 1
            
        return count
