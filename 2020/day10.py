from utils.aoc_utils import AOCDay

class Day10(AOCDay):
    def common(self):
        numbers = []
        for line in self.inputData:
            numbers.append(int(line))

        self.inputData = numbers
        self.inputData.sort()

        max = self.inputData[len(self.inputData) - 1] + 3
        self.inputData.append(max)

    def part1(self):
        diff1 = 0
        diff3 = 0

        current = 0

        for joltage in self.inputData:
            diff = joltage - current

            if diff == 1:
                diff1 +=1
            elif diff == 3:
                diff3 += 1

            current = joltage

        return diff1 * diff3


    def part2(self):
        poss = {0:1}

        for jolt in self.inputData:
            poss[jolt] = 0

            if jolt - 1 in poss:
                poss[jolt]+=poss[jolt-1]
            if jolt - 2 in poss:
                poss[jolt]+=poss[jolt-2]
            if jolt - 3 in poss:
                poss[jolt]+=poss[jolt-3]

        return poss[self.inputData[len(self.inputData) - 1]]