from utils.aoc_utils import AOCDay

class Day10(AOCDay):
    def common(self):
        # Input is already in a workable format :)
        return 0


    def part1(self):
        scoreDic = {
            '': 0,
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

        return sum([scoreDic[checkForSyntaxError(line)] for line in self.inputData])
    

    def part2(self):
        incompleteLines = [line for line in self.inputData if checkForSyntaxError(line) == '']

        for line in incompleteLines:
            result = completeLine(line)
            print(result)
            
        return 0


# Check if there is a syntax error in the provided line. Will return the faulty character if found or '' otherwise
def checkForSyntaxError(line):
    isSyntaxError, faultyCharIndex = checkForSyntaxErrorRec(line, line[0], 0)
    return line[faultyCharIndex] if isSyntaxError else ''


def checkForSyntaxErrorRec(line, parentChar, parentIndex):
    openingChars = ['(', '[', '{', '<']
    closingChars = [')', ']', '}', '>']

    closeParent = closingChars[openingChars.index(parentChar)]

    # Loop until we close the parent char or until the end of the line
    curIndex = parentIndex + 1
    while curIndex < len(line) and line[curIndex] != closeParent:
        # If we find another closingChars, its a syntax error
        if line[curIndex] in closingChars:
            return (True, curIndex)
        
        # Check syntax of the nested chunk
        isSyntaxError, index = checkForSyntaxErrorRec(line, line[curIndex], curIndex)
        if (isSyntaxError): 
            return (True, index)

        # If there is no syntax error in the nested chunk, continue looping at the end of it
        curIndex = index + 1
    
    # We reached the end of this chunk, return that there was no syntax error and the index of the closeParent
    return (False, curIndex)



def completeLine(line):
    notClosed = []
    completeLineRec(line, line[0], 0, notClosed)

    return notClosed

def completeLineRec(line, parentChar, parentIndex, notClosed):
    openingChars = ['(', '[', '{', '<']
    closingChars = [')', ']', '}', '>']

    closeParent = closingChars[openingChars.index(parentChar)]

    # Loop until we close the parent char or until the end of the line
    curIndex = parentIndex + 1
    while curIndex < len(line) and line[curIndex] != closeParent:
        # Check completeness of the nested chunk
        isComplete, index = completeLineRec(line, line[curIndex], curIndex, notClosed)
        if (not isComplete): 
            notClosed.append(line[index])
            return (False, parentIndex)

        # If there is no syntax error in the nested chunk, continue looping at the end of it
        curIndex = index + 1
    
    # If we are at the end of the line, this chunk is incomplete
    if curIndex == len(line):
        return (False, parentIndex)

    # Else we reached the end of this chunk, return that it is complete and the index of the closeParent
    return (True, curIndex)