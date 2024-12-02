from numpy.lib.shape_base import apply_along_axis
from utils.aoc_utils import AOCDay
import numpy as np

class Day3(AOCDay):
    def common(self):
        # Make a matrix of boolean values
        allLines = []
        for line in self.inputData:
            allLines.append([bit == "1" for bit in line])
        
        # Transfer that matrix to np format
        self.bitMatrix = np.array(allLines)
        self.rows = self.bitMatrix.shape[0]
        self.columns = self.bitMatrix.shape[1]
        
        return 0

    def part1(self):
        gamma = ""
        for i in range(self.columns):
            # Bit sum of the column
            ones = sum(self.bitMatrix[:,i])
            # Check if the number of ones is greater than the number of zeros
            condition = ones > self.rows - ones
            gamma += str(int(condition))
        
        # Inverting bits of the gamma factor
        epsilon = "".join(["0" if x == "1" else "1" for x in gamma])

        return int(gamma, 2) * int(epsilon, 2)
    
    
    def applyBitCriteriaRec(self, n, matrix, isMostCommon):
        rows = matrix.shape[0]
        columns = matrix.shape[1]

        # Base case: only one left, return it        
        if rows == 1:
            return matrix[0,:]
        
        # Induction step: apply bit criteria
        
        ones = sum(matrix[:,n])
        # Check if the number of ones is greater than the number of zeros
        valueToKeep = ones >= rows - ones
        
        # Inverting value to keep depending of the parameter we have
        if (not isMostCommon):
            valueToKeep = not valueToKeep
        
        # In reverse order to not fuck up indexes while deleting
        rowsToDelete = [i for i in range(rows-1, -1, -1) if matrix[i,n] != valueToKeep]
        for rowI in rowsToDelete:
            matrix = np.delete(matrix, rowI, 0)
                
        n += 1
        
        result = self.applyBitCriteriaRec(n, matrix, isMostCommon)
        return "".join([str(int(bit)) for bit in result])
    
    
    def part2(self):        
        oxygen = self.applyBitCriteriaRec(0, self.bitMatrix, True)
        
        co2 = self.applyBitCriteriaRec(0, self.bitMatrix, False)

        return int(oxygen, 2) * int(co2, 2)