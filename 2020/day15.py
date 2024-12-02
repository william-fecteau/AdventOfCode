from utils.aoc_utils import AOCDay

class Day15(AOCDay):
    def common(self):
        self.spokenNumbers = []

        for num in self.inputData[0].split(','):
            self.spokenNumbers.append(int(num))

    def part1(self):
        return self.play(2020)

    def part2(self):
        return self.play(30000000)

    def play(self, times):
        dicHistory = {}
        for i in range(len(self.spokenNumbers)):
            dicHistory[self.spokenNumbers[i]] = [i]

        for currentTurn in range(len(self.spokenNumbers), times):
            oldNum = self.spokenNumbers[currentTurn - 1]
            newNum = 0

            occ = 0
            if oldNum in dicHistory:
                occ = len(dicHistory[oldNum])

            if occ > 1:
                iOcc = dicHistory[oldNum][occ - 2] + 1
                newNum = currentTurn - iOcc
            
            if newNum not in dicHistory:
                dicHistory[newNum] = []

            self.spokenNumbers.append(newNum)
            dicHistory[newNum].append(currentTurn)

        return self.spokenNumbers[len(self.spokenNumbers) - 1]