import numpy as np
from utils.aoc_utils import AOCDay

class Day6(AOCDay):
    def common(self):
        self.map = np.array([[char for char in line] for line in self.inputData])

    def step(self, guard_pose):
        theta = guard_pose[2]
        if theta == 0:
            step = np.array([-1, 0, 0])
        elif theta == 90:
            step = np.array([0, 1, 0])
        elif theta == 180:
            step = np.array([1, 0, 0])
        elif theta == 270:
            step = np.array([0, -1, 0])
        
        new_pose = guard_pose + step
        new_i, new_j, _ = new_pose

        # Out of bounds
        if new_i < 0 or new_i >= self.map.shape[1] or new_j < 0 or new_j >= self.map.shape[0]:
            return None 

        # Turn right at obstacle
        if self.map[new_i, new_j] == "#":
            new_pose = guard_pose + np.array([0, 0, 90])
            new_pose[2] %= 360
            return new_pose

        return new_pose


    def part1(self):
        guard_pose = None
        for i, line in enumerate(self.map):
            for j, cell in enumerate(line):
                if cell == "^":
                    guard_pose = np.array([i, j, 0])
                    break
        
        while guard_pose is not None:
            self.map[guard_pose[0], guard_pose[1]] = "X"
            guard_pose = self.step(guard_pose)

        print(self.map)

        return np.count_nonzero(self.map == "X")

    def part2(self):
        return 0
