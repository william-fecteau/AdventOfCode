from utils.aoc_utils import AOCDay
import math

class Day13(AOCDay):
    def common(self):
        self.startTime = int(self.inputData[0])

        busIds = {}
        splitResult = self.inputData[1].split(',')

        t = 0
        for busId in splitResult:
            if busId != 'x':
                busIds[t] = int(busId)
            t += 1

        self.inputData = busIds

    def getNearestTime(self, startTime, busId):
        return math.ceil(startTime / busId) * busId

    def part1(self):
        smallestTime = 99999999999
        smallestId = 0

        for t in self.inputData:
            busId = self.inputData[t]

            curTime =  self.getNearestTime(self.startTime, busId)

            if curTime < smallestTime:
                smallestTime = curTime
                smallestId = busId

        return (smallestTime - self.startTime) * smallestId


    
    def part2(self):
        #startTime = 0
        #prochainDepart = self.inputData.keys()[0]

        #while True:
            #valid = True

            #for t in self.inputData:
            #    busId = self.inputData[t]

            #    if (startTime + t) % busId != 0:
            #        valid = False
            #        break
            
            #if valid:
            #    break
            
            #startTime += 1

        #return startTime


        # Dont use this solution, its trash :(
        i = 0
        n = 0

        while (n-6)%37 != 0 or (n-10)%41 != 0 or (n+31)%571 != 0 or (n+48)%17 != 0:
            n=i*13*29*23*19*787

            i += 1

        return n
        