from utils.aoc_utils import AOCDay
import numpy as np
import copy

class Day4(AOCDay):
    def common(self):
        # Getting only the ball order
        self.ballOrder = [int(x) for x in self.inputData[0].split(',')]
        
        # Removing ball order and empty spaces (We know that each bingo card is 5x5, so five lines)       
        self.inputData = [i for i in self.inputData[1::] if i != ""]
        
        # Getting all bingo cards in a np matrix. Each value is a tuple (number, isMarked)
        self.allBingoCards = []
        curBingoCard = []
        for i, line in enumerate(self.inputData):
            if i != 0 and i % 5 == 0:
                self.allBingoCards.append(np.array(curBingoCard))
                curBingoCard = []
                
            curBingoCard.append([(int(line[j:j+3]), False) for j in range(0, len(line), 3)]) # Slice every three chars. int conversion works if there is a space at the end!
        
        # Don't forget to add the last board, that was painful to debug :(
        self.allBingoCards.append(np.array(curBingoCard))

        return 0

    # Looping through bingo card and check if the number is present. If it is, return its position in the card
    def markNumber(self, bingoCard, number):
        for i, row in enumerate(bingoCard):
            for j, cell in enumerate(row):
                value, isMarked = cell
                
                if (number == value):
                    bingoCard[i, j] = (value, True)
                    return (i, j)

        return (-1, -1)

    # After marking a number at position markedTuple, check if the board is winning
    def isWinning(self, bingoCard, markedTuple):
        i, j = markedTuple
        
        # Taking second value, which represents if the card was marked
        row = [x[1] for x in bingoCard[i,:]]
        column = [x[1] for x in bingoCard[:,j]]
        
        return sum(row) == 5 or sum(column) == 5

    def calculateScore(self, bingoCard):
        score = 0
        for i in range(5):
            score += sum([x[0] for x in bingoCard[i,:] if not x[1]])
        
        return score

    def part1(self):
        # Make sure we got a deep copy because we need it in part 2
        bingoCardsCopy = copy.deepcopy(self.allBingoCards)
        
        score = -1
        for num in self.ballOrder:
            for bingoCard in bingoCardsCopy:
                markedPos = self.markNumber(bingoCard, num)
                if markedPos != (-1, -1) and self.isWinning(bingoCard, markedPos):
                    # Winning condition
                    score = self.calculateScore(bingoCard)
                    break
                
            if (score != -1):
                return score * num
            
        return -1
    
    def part2(self):
        lastCard = None
        lstWinners = []
        for num in self.ballOrder:
            for i, bingoCard in enumerate(self.allBingoCards):
                # Don't play cards that already won
                if i in lstWinners:
                    continue

                markedPos = self.markNumber(bingoCard, num)
                if markedPos != (-1, -1) and self.isWinning(bingoCard, markedPos):
                    # Winning condition
                    lastCard = bingoCard
                    lstWinners.append(i)

                
            if (len(lstWinners) == len(self.allBingoCards)):
                score = self.calculateScore(lastCard)
                
                return score * num
            
        return -1