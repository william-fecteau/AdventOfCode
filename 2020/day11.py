from utils.aoc_utils import AOCDay

class Day11(AOCDay):
    def common(self):
        return 0

    def getNeighbours(self, matrix, i, j):
        occupied = 0
        directions = [(0, -1), (0, 1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1)]

        # Pour chacune des 8 directions
        for direction in directions:
            i2 = i + direction[0]
            j2 = j + direction[1]

            # Si le siège n'est pas out of bound et qu'il s'agit d'un '#'
            if i2 >= 0 and j2 >= 0 and i2 <= len(matrix) - 1 and j2 <= len(matrix[0]) - 1 and matrix[i2][j2] == '#':
                occupied += 1

        return occupied


    def getOccupiedSeatInSight(self, matrix, i , j):
        occupied = 0
        directions = [(0, -1), (0, 1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1)]

        # Pour chacune des 8 directions
        for direction in directions:      
            i2 = i + direction[0]
            j2 = j + direction[1]

            # On continu tant qu'on est pas out of bound
            while i2 >= 0 and j2 >= 0 and i2 <= len(matrix) - 1 and j2 <= len(matrix[0]) - 1:
                # Si on trouve un '#' ou un 'L' on break
                if matrix[i2][j2] == '#':
                    occupied += 1
                    break
                elif matrix[i2][j2] == 'L':
                    break

                # Si c'est un '.' on continue
                i2 += direction[0]
                j2 += direction[1]

        return occupied

    def iteration(self, seatMatrix, neighbourFunc, nbUntilFree):
        newSeatMatrix = []

        for i in range(len(seatMatrix)):
            newSeatMatrix.append([])
            for j in range(len(seatMatrix[0])):
                qtNeightbours = neighbourFunc(seatMatrix, i, j)

                if seatMatrix[i][j] == 'L' and qtNeightbours == 0:
                    newSeatMatrix[i].append('#')
                elif seatMatrix[i][j] == '#' and qtNeightbours >= nbUntilFree:
                    newSeatMatrix[i].append('L')
                else:
                    newSeatMatrix[i].append(seatMatrix[i][j])

        return newSeatMatrix

    def part1(self):
        oldSeatMatrix = self.inputData
        seatMatrix = self.iteration(oldSeatMatrix, self.getNeighbours, 4)

        while seatMatrix != oldSeatMatrix:
            oldSeatMatrix = seatMatrix
            seatMatrix = self.iteration(oldSeatMatrix, self.getNeighbours, 4)

        occupied = 0
        for line in seatMatrix:
            occupied += line.count('#')

        return occupied
    
    def part2(self):
        oldSeatMatrix = self.inputData
        seatMatrix = self.iteration(oldSeatMatrix, self.getOccupiedSeatInSight, 5)

        while seatMatrix != oldSeatMatrix:
            oldSeatMatrix = seatMatrix
            seatMatrix = self.iteration(oldSeatMatrix, self.getOccupiedSeatInSight, 5)

        occupied = 0
        for line in seatMatrix:
            occupied += line.count('#')

        return occupied