from utils.aoc_utils import AOCDay

class Day3(AOCDay):
    def common(self):
        matrix = []

        self.xLength = len(self.inputData[0])
        self.yLength = len(self.inputData)

        for line in self.inputData:
            ligne = []
            
            for char in line:
                ligne.append(bool(char == '#'));

            matrix.append(ligne)

        self.inputData = matrix

    def iteration(self, xStep, yStep):
        x = 0
        y = 0

        cptTree = 0

        while y < self.yLength - 1:
            x += xStep
            y += yStep

            if(self.inputData[y][x % self.xLength]):
                cptTree += 1

        return cptTree


    def part1(self):
        return self.iteration(3, 1)
    
    
    def part2(self):
        slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
        total = 1

        for slope in slopes:
            total *= self.iteration(slope[0], slope[1])
        
        return total