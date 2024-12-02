from numpy.core.fromnumeric import sort
from utils.aoc_utils import AOCDay
import numpy as np

class Day9(AOCDay):
    def common(self):
        rows = []
        for line in self.inputData:
            rows.append([int(num) for num in line])
        
        self.heightMap = np.array(rows)


    def part1(self):
        # Keeping lowPoints in index form because we're gonna need it in part2
        self.lowPoints = []
        for i, row in enumerate(self.heightMap):
            for j, point in enumerate(row):
                neighbors = getNeighbors(self.heightMap, i, j)

                # Check if all neighbors are greater than the point itself
                if all(point < self.heightMap[nI, nJ] for nI, nJ in neighbors):
                    self.lowPoints.append((i, j))

        # Sum of risk levels
        return sum([self.heightMap[x, y] + 1 for x, y in self.lowPoints])


    def part2(self):
        lstBassin = []
        for i, j in self.lowPoints:
            bassinSize = exploreBassin(self.heightMap, i, j, [])
            lstBassin.append(bassinSize)

        threeBiggest = sorted(lstBassin, reverse=True)[0:3]
        return np.prod(threeBiggest)


# Return the indexes of all the neighbors of a given point
def getNeighbors(matrix, i, j):
    neighbors = []
    
    allDirections = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nbRows, nbColumns = np.shape(matrix)
    for direction in allDirections:
        offI = i + direction[0] # Rows
        offJ = j + direction[1] # Cols

        # Check that the point is in bound of the matrix
        if (offI < 0 or offI >= nbRows): continue
        if (offJ < 0 or offJ >= nbColumns): continue
        
        neighbors.append((offI, offJ))

    return neighbors


# Start from a low point and return the size of the bassin
def exploreBassin(matrix, i, j, exploredList):
    point = matrix[i, j]
    
    # Base case, we encounter a 9 or an already explored point
    if point == 9 or (i, j) in exploredList: 
        return 0

    # Explore each neigbors sub-bassin
    bassinSize = 1
    exploredList.append((i, j))
    for nI, nJ in  getNeighbors(matrix, i, j):
        bassinSize += exploreBassin(matrix, nI, nJ, exploredList)

    return bassinSize