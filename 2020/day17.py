from utils.aoc_utils import AOCDay

class Day17(AOCDay):
    def common(self):
        self.initialState = []
        self.xLenght = len(self.inputData[0])
        self.yLenght = len(self.inputData)

        for line in self.inputData:
            parsedLine = []
            for char in line:
                active = True if char == '#' else False
                parsedLine.append(active)
            
            self.initialState.append(parsedLine)

    def generateEmptySlice(self):
        emptySlice = []

        for i in range(self.yLenght):
            emptySlice.append([False] * self.xLenght)

        return emptySlice

    def getNeighbors(self, x, y, z):
        lstNeighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    nX = x + i
                    nY = y + j
                    nZ = z + k

                    if nX < self.xLenght and nX >= 0 and nY < self.yLenght and nY >= 0 and nZ < len(self.pocketSpace) and nZ >= 0:
                        lstNeighbors.append([nX, nY, nZ])
        
        lstNeighbors.remove([x, y, z])

        return lstNeighbors

    def countActiveCube(self, lstPoint):
        counter = 0

        for point in lstPoint:
            x = point[0]
            y = point[1]
            z = point[2]

            if self.pocketSpace[z][y][x]:
                counter += 1

        return counter



    def iteration(self):
        newPocketSpace = []
        for i in range(len(self.pocketSpace)):
            newPocketSpace.append(self.generateEmptySlice())

        for z in range(len(self.pocketSpace)):
            for y in range(len(self.pocketSpace[z])):
                for x in range(len(self.pocketSpace[z][y])):
                    #print(str(x) + " " + str(y) + " " + str(z))
                    neighbors = self.getNeighbors(x, y, z)

                    count = self.countActiveCube(neighbors)

                    currentCubeState = self.pocketSpace[z][y][x]

                    # Si actif
                    if currentCubeState and count != 2 and count != 3:
                        currentCubeState = False
                    elif not currentCubeState and count == 3:
                        currentCubeState = True

                    newPocketSpace[z][y][x] = currentCubeState
        
        self.pocketSpace = newPocketSpace
                        

    def printSlices(self):
        for i in range(len(self.pocketSpace)):
            print("-----------------" + str(i) + "-----------------")
            for j in range(len(self.pocketSpace[i])):
                for k in self.pocketSpace[i][j]:
                    if k:
                        print('#', end='')
                    else:
                        print('.', end='')
                print("")



    def part1(self):
        self.pocketSpace = []
        self.pocketSpace.append(self.initialState)

        self.pocketSpace.insert(0, self.generateEmptySlice())
        self.pocketSpace.append(self.generateEmptySlice())


        self.iteration()

        self.printSlices()

        return 0
    
    def part2(self):
        return 0