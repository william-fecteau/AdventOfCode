from utils.aoc_utils import AOCDay

class Day1(AOCDay):
    def common(self):
        self.sonarSweep = [int(x) for x in self.inputData]
        return 0

    def getGreaterCount(self, intList):
        # Comparing each element with the next to see if the next element is greater
        result = map(lambda a, b: a < b, intList, intList[1:len(intList)])
        
        # Sum of all the boolean values, will return the count of a < b
        return sum(list(result))

    def part1(self):
        return self.getGreaterCount(self.sonarSweep)
    
    def part2(self):
        # Creating a new list where each element is a sum of three element from self.sonarSweep
        sonarSweepOfThree = [sum(self.sonarSweep[i:i+3]) for i in range(len(self.sonarSweep)-2)]
                                
        # Same operation as part 1, but a different list
        return self.getGreaterCount(sonarSweepOfThree)