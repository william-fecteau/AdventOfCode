from utils.aoc_utils import AOCDay

class Day8(AOCDay):
    def common(self):
        self.outputValues = []
        self.signalPatterns = []
        for line in self.inputData:
            signalPattern, output = line.split(' | ')
            
            self.signalPatterns.append([digit for digit in signalPattern.split(' ')])
            self.outputValues.append([digit for digit in output.split(' ')])

    def part1(self):
        count = 0
        for output in self.outputValues:
            count += sum([len(x) in [2, 3, 4, 7] for x in output])
        return count

    def filterByLength(self, digit, length):
        return list(filter(lambda x: len(x) == length, digit)) 
    
    def part2(self):
        # Here is my digit indexation for segments
        # .0.
        # 1.2
        # .3.
        # 4.5
        # .6.
        
        for i, digit in enumerate(self.signalPatterns):
            segments = [-1] * 7
            one = set(self.filterByLength(digit, 2)[0])
            four = set(self.filterByLength(digit, 4)[0])
            seven = set(self.filterByLength(digit, 3)[0])
            eight = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
            possibleSix = [set(x) for x in self.filterByLength(digit, 6)]
            possibleThree = [set(x) for x in self.filterByLength(digit, 5)]

            # Finding six knowing that six only has one of the two segment of one (Other digit with 6 segment perfectly intersect it)
            six = -1
            for d in possibleSix:
                if len(d.intersection(one)) == 1:
                    six = d

            # Finding three knowing that three perfectly intersect with five (Other digit with 5 segment do not perfectly intersect it)
            three = -1
            for d in possibleThree:
                if len(d.intersection(seven)) == 3:
                    three = d

            # Find segment 0 with (seven \ one)
            segments[0] = seven.difference(one).pop()
    
            # Find segment 2 and 5 with (one \ six) and (one ∩ six)
            segments[2] = one.difference(six).pop()
            segments[5] = one.intersection(six).pop()
        
            # Find segment 3 with some more set theory
            segments[3] = three.difference(seven).intersection(four).pop()
            
            # Find segment 1, moooooooar set theory
            segments[1] = four.difference(one).difference(set(segments[3])).pop()
            
            # Find segment 6, my brain is frying
            segmentSet = {segments[0], segments[2], segments[5], segments[3], segments[1]}
            segments[6] = three.difference(segmentSet).pop()

            # Fiouf last segment, king of bruteforcing it at this point lol
            segmentSet.add(segments[6])
            segments[4] = eight.difference(segmentSet).pop()
            
            # Hardcoding remaining digit cause we have all segments
            two = {segments[0], segments[2], segments[3], segments[4], segments[6]}
            five = {segments[0], segments[1], segments[3], segments[5], segments[6]}
            nine = {segments[0], segments[1], segments[2], segments[3], segments[5], segments[6]}
            zero = {segments[0], segments[1], segments[2], segments[4], segments[5], segments[6]}
            
            # Reading output
            print(segments)
            
        return 0