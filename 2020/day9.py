from utils.aoc_utils import AOCDay

class Day9(AOCDay):
    def common(self):
        numbers = []
        for line in self.inputData:
            numbers.append(int(line))

        self.inputData = numbers

    def part1(self):
        preambleStep = 25

        for i in range(preambleStep, len(self.inputData)):
            target = self.inputData[i]

            preamble = []
            for j in range(i - preambleStep, i):
                preamble.append(self.inputData[j])

            valid = False
            for num in preamble:
                if target - num in preamble:
                    valid = True
                    break

            if not valid:
                self.target = target
                return target
            
    
    def part2(self):
        for i in range(len(self.inputData)):
            somme = self.inputData[i]
            largest = self.inputData[i]
            smallest = self.inputData[i]

            for j in range(i + 1, len(self.inputData)):
                somme += self.inputData[j]

                if largest < self.inputData[j]:
                    largest = self.inputData[j]
                
                if smallest > self.inputData[j]:
                    smallest = self.inputData[j]

                if somme > self.target:
                    break
                elif somme == self.target:
                    return largest + smallest

        return -1