import math
from utils.aoc_utils import AOCDay

class Day12(AOCDay):
    def common(self):
        return 0

    # Direction : N, E, S, O
    def goTo(self, direction, unit):
        if direction == 'N':
            self.y += unit
        elif direction == 'S':
            self.y -= unit
        elif direction == 'E':
            self.x += unit
        elif direction == 'W':
            self.x -= unit
        elif direction == 'F':
            self.x = self.x + unit * self.pointing[0]
            self.y = self.y + unit * self.pointing[1]
        

    # Direction : L, R
    def turnAround(self, direction, degree):
        tempPx = self.pointing[0]
        tempPy = self.pointing[1]

        rad = math.radians(degree)

        if direction == 'R':
            rad = -rad

        self.pointing[0] = int(tempPx * math.cos(rad) - tempPy * math.sin(rad))
        self.pointing[1] = int(tempPx * math.sin(rad) + tempPy * math.cos(rad))

    def part1(self):
        self.pointing = [1, 0]
        self.x = 0
        self.y = 0

        for line in self.inputData:
            direction = line[0]
            unit = int(line[1:])

            if direction == 'L' or direction == 'R':
                self.turnAround(direction, unit)
            else:
                self.goTo(direction, unit)
        
        return abs(self.x) + abs(self.y)
    


    def moveWaypoint(self, direction, unit):
        if direction == 'N':
            self.wy += unit
        elif direction == 'S':
            self.wy -= unit
        elif direction == 'E':
            self.wx += unit
        elif direction == 'W':
            self.wx -= unit
        elif direction == 'F':
            self.x += unit * self.wx
            self.y += unit * self.wy

    def turnWaypoint(self, direction, degree):
        tempPx = self.wx
        tempPy = self.wy

        rad = math.radians(degree)

        if direction == 'R':
            rad = -rad

        self.wx = tempPx * math.cos(rad) - tempPy * math.sin(rad)
        self.wy = tempPx * math.sin(rad) + tempPy * math.cos(rad)


    # 16 629 too low
    def part2(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1


        for line in self.inputData:
            direction = line[0]
            unit = int(line[1:])

            if direction == 'L' or direction == 'R':
                self.turnWaypoint(direction, unit)
            else:
                self.moveWaypoint(direction, unit)
        
        return abs(self.x) + abs(self.y)