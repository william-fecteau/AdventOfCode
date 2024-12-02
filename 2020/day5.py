from utils.aoc_utils import AOCDay

class Day5(AOCDay):
    def common(self):
        ticket = []

        for line in self.inputData:
            line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
            ticket.append(line)

        self.inputData = ticket

    def strToBin(self, strBin):
        somme = 0
        strBin = strBin[::-1]

        for i in range(len(strBin)):
            bit = int(strBin[i])
            somme += bit*(2**i)

        return somme

    def getTicketID(self, strTicket):
        strRow = strTicket[:7]
        strCol = strTicket[-3:]
        row = int(self.strToBin(strRow))
        col = int(self.strToBin(strCol))

        return row * 8 + col

    def part1(self):
        maxSeatid = -999

        for ticket in self.inputData:
            seatID = self.getTicketID(ticket)

            if seatID > maxSeatid:
                maxSeatid = seatID

        return maxSeatid
    
    def part2(self):
        allTickets = []
        for i in range(128):
            for j in range(8):
                allTickets.append(i * 8 + j)

        for ticket in self.inputData:
            seatID = self.getTicketID(ticket)

            if seatID != 1 and seatID != -1:
                allTickets.remove(seatID)

        for i in range(len(allTickets)):
            if i != 0 and i != len(allTickets):
                if allTickets[i-1] != allTickets[i] - 1 and allTickets[i+1] != allTickets[i] + 1:
                    return allTickets[i]

        return -1