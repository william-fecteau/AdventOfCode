from utils.aoc_utils import AOCDay
import numpy as np

class Day5(AOCDay):
    def common(self):        
        self.ventLines = []
        for line in self.inputData:
            lineStart, lineEnd = line.split(" -> ")
            startX, startY = lineStart.split(",")
            endX, endY = lineEnd.split(",")
            self.ventLines.append([(int(startX), int(startY)), (int(endX), int(endY))])

        # Build seaMap with only horizontal/vertical     
        self.seaMap = np.zeros((1000,1000))
        self.buildSeaMap(self.seaMap, False)
        
        return 0

    # Takes a sea map and if we want to build only diagonal or only horizontal/vertical
    def buildSeaMap(self, seaMap, onlyDiagonals):        
        for line in self.ventLines:
            startX, startY = line[0]
            endX, endY = line[1]
            
            # If we are interested only in diagonals, ignore horizontal/vertical
            if onlyDiagonals and (startX == endX or startY == endY):
                continue
            # If we are interested only in horizontal/vertical, ignore diagonals
            if not onlyDiagonals and startX != endX and startY != endY:
                continue
            
            stepX = endX - startX
            stepY = endY - startY
            
            if (stepX != 0):
                stepX = 1 if stepX > 0 else -1
            if (stepY != 0):
                stepY = 1 if stepY > 0 else -1
            
            while startX != endX or startY != endY:
                seaMap[startY, startX] += 1
                startX += stepX
                startY += stepY
            
            # Don't forget to add the last one
            seaMap[startY, startX] += 1


    def countOverlapInSeaMap(self, seaMap):
        counter = 0
        for row in seaMap:
            for elem in row:
                if elem > 1:
                    counter += 1
        
        return counter


    def part1(self):
        return self.countOverlapInSeaMap(self.seaMap)
    
    def part2(self):
        # Keep the same map as part 1, but only build the diagonals
        self.buildSeaMap(self.seaMap, True)
        return self.countOverlapInSeaMap(self.seaMap)