from utils.aoc_utils import AOCDay

class Day16(AOCDay):
    def common(self):
        self.validBounds = {}
        i = 0
        line = self.inputData[i]

        while line != "":
            line = line.replace(' ', '')

            name, bounds = line.split(':')

            bounds = bounds.split('or')

            lstBounds = []
            for bound in bounds:
                bound = bound.split('-')
                lstBounds.append(int(bound[0]))
                lstBounds.append(int(bound[1]))

            self.validBounds[name] = lstBounds

            i += 1
            line = self.inputData[i]

        # Get ticket line
        i += 2
        self.yourTicket = []
        for field in self.inputData[i].split(','):
            self.yourTicket.append(int(field))


        # Get nearby tickets
        start = i + 3
        self.nearbyTickets = []
        for i in range(start, len(self.inputData)):
            ticket = []
            for field in self.inputData[i].split(','):
                ticket.append(int(field))
            
            self.nearbyTickets.append(ticket)


    def getInvalidFields(self, ticket):
        invalidFields = []

        for field in ticket:
            for fieldName in self.validBounds:
                bounds = self.validBounds[fieldName]
                valid = False

                if (field >= bounds[0] and field <= bounds[1]) or (field >= bounds[2] and field <= bounds[3]):
                    valid = True
                    break

            if not valid:
                invalidFields.append(field)
                break
        return invalidFields

    def part1(self):
        somme = 0

        self.validNearbyTickets = []

        for ticket in self.nearbyTickets:
            invalidFields = self.getInvalidFields(ticket)

            if len(invalidFields) > 0:
                for field in invalidFields:
                    somme += field
            else:
                self.validNearbyTickets.append(ticket)


        return somme
    

    def part2(self):
        allPossibilities = {}
        for fieldName in self.validBounds:
            allPossibilities[fieldName] = []
            bounds = self.validBounds[fieldName]

            for i in range(len(self.validNearbyTickets)):
                possibilities = []
                ticket = self.validNearbyTickets[i]

                for j in range(len(ticket)):
                    field = ticket[j]
                    if (field >= bounds[0] and field <= bounds[1]) or (field >= bounds[2] and field <= bounds[3]):
                        possibilities.append(j)

                allPossibilities[fieldName].append(possibilities)
        
            allPossibilities[fieldName] = list(set.intersection(*map(set, allPossibilities[fieldName])))
        
        result = {}

        while len(result) != len(allPossibilities):
            for fieldName in allPossibilities:
                if len(allPossibilities[fieldName]) == 1:
                    index = allPossibilities[fieldName][0]
                    result[fieldName] = index

                    for fieldName2 in allPossibilities:
                        if index in allPossibilities[fieldName2]:
                            allPossibilities[fieldName2].remove(index)

        product = 1
        for fieldName in result:
            if fieldName.startswith("departure"):
                product *= self.yourTicket[result[fieldName]]

        return product