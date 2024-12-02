from utils.aoc_utils import AOCDay

class Day14(AOCDay):
    def common(self):
        return 0

    def parseMask(self, strMask):
        mask = {}

        for i in range(36):
            mask[i] = strMask[i]

        return mask

    def convertCharArrToStr(self, charArray):
        strResult = ""

        for char in charArray:
            strResult += str(char)

        return strResult

    def getAllPossibilities(self, binValue):
        masks = []

        if 'X' in binValue:
            p1, p2 = binValue.replace('X', '0', 1), binValue.replace('X', '1', 1)
            masks.extend(self.getAllPossibilities(p1))
            masks.extend(self.getAllPossibilities(p2))
        else:
            masks.append(binValue)

        return masks

    def executeLine(self, line, mask):
        line = line.replace(' ', '')

        adress, binValue = line.split('=')

        adress = adress.split(']')
        adress = adress[0].split('[')
        adress = adress[1]

        # Converting value to char array
        binValue = list(bin(int(binValue)).replace('0b', ''))
        while len(binValue) < 36:
            binValue.insert(0, 0)

        # Applying mask to value
        for bit in mask:
            if mask[bit] != 'X':
                binValue[bit] = mask[bit]

        # Converting char array to string
        strBitValue = ""
        for bit in binValue:
            strBitValue += str(bit)

        value = int(strBitValue, 2)
        self.memory[adress] = value
        








    def executeLine2(self, line, mask):
        line = line.replace(' ', '')

        adress, binValue = line.split('=')

        adress = adress.split(']')
        adress = adress[0].split('[')
        adress = adress[1]

        value = int(binValue)


        # Converting adress to char array
        binAdress = list(bin(int(adress)).replace('0b', ''))
        while len(binAdress) < 36:
            binAdress.insert(0, 0)

        # Applying mask to adress
        for bit in mask:
            if mask[bit] != "0":
                binAdress[bit] = mask[bit]

        # Converting char array to string
        strBinAdress = self.convertCharArrToStr(binAdress)

        adressPosibilities = self.getAllPossibilities(strBinAdress)
        for possibility in adressPosibilities:
            self.memory[int(possibility, 2)] = value


        

    def part1(self):
        self.memory= {}
        currentMask = {}

        for line in self.inputData:
            if line.startswith('mask = '):
                strMask = line[-36:]
                currentMask = self.parseMask(strMask)
            else:
                self.executeLine(line, currentMask)
        
        somme = 0
        for adress in self.memory:
            somme += self.memory[adress]

        return somme
    

    # 483697443945070 too high
    # 2246131425692179 too high
    # 2246131425692179
    def part2(self):
        self.memory= {}
        currentMask = {}

        for line in self.inputData:
            if line.startswith('mask = '):
                strMask = line[-36:]
                currentMask = self.parseMask(strMask)
            else:
                self.executeLine2(line, currentMask)
        
        somme = 0
        for adress in self.memory:
            somme += self.memory[adress]

        return somme