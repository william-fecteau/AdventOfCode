from utils.aoc_utils import AOCDay

class Day7(AOCDay):
    def common(self):
        # Liste de toutes les règles:
        # Structure d'une règle
        # "ruleName": "couleur"
        # "holding": [{"name": "couleur", "qt": "1"}]
        lstRules = []

        for line in self.inputData:
            dicRule = {}

            # On retire les espaces et les points
            line = line.replace(' ', '').replace('.', '')
            # On sépare le nom de ce que le sac peut contenir
            name, holding = line.split('bagscontain')

            # Création de la liste pour ce que le sac peut contenir
            lstContainers = []
            
            # Si ce n'est pas aucun sac
            if holding != "nootherbags":
                # On split sur toutes les virgules et on parcours chaque item
                holding = holding.split(',')
                for contain in holding:
                    dicHolding = {}
                    contain = contain.replace('bags', '').replace('bag', '')
                    qt = int(contain[0])
                    nameContained = contain[1:]
                    dicHolding["name"] = nameContained
                    dicHolding["qt"] = qt
                    lstContainers.append(dicHolding)

            dicRule["ruleName"] = name
            dicRule["holding"] = lstContainers
            lstRules.append(dicRule)

        self.inputData = lstRules



    def canHold(self, bagName, lstCanHold):
        for rule in self.inputData:
            if rule["name"] == bagName:
                continue
            else:
                lstContainers = rule["containers"]
                for bag in lstContainers:
                    if bag["name"] == bagName and rule["name"] not in lstCanHold:
                        lstCanHold.append(rule["name"])
                        lstCanHold = self.canHold(rule["name"], lstCanHold)
                        break;

        return lstCanHold
                
    def countBag(self, bagName):
        total = 0

        for rule in self.inputData:
            if rule["name"] == bagName:
                lstContainers = rule["containers"]
                for bag in lstContainers:
                    total += bag["qt"]
                    total += bag["qt"] * self.countBag(bag["name"])

        return total



    def part1(self):
        return len(self.canHold("shinygold", []))
    
    def part2(self):
        return self.countBag("shinygold")