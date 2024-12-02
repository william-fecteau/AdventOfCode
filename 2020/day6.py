from utils.aoc_utils import AOCDay
from string import ascii_lowercase

class Day6(AOCDay):
    def common(self):
        lstGroupe = []

        lstPersonnes = []

        for line in self.inputData:
            if line != "":
                lstPersonnes.append(line)
            else:
                lstGroupe.append(lstPersonnes)
                lstPersonnes = []

        lstGroupe.append(lstPersonnes)

        self.inputData = lstGroupe


    def part1(self):
        cpt = 0
        for group in self.inputData:
            yes = []
            for personne in group:
                for rep in personne:
                    if rep in yes:
                        yes.append(rep)

            cpt += len(yes)
        return cpt
    


    def part2(self):
        totalCpt = 0

        for group in self.inputData:
            cpt = 0
            for letter in ascii_lowercase:
                valid = True

                for personne in group:
                    if letter not in personne:
                        valid = False
                        break
                
                if valid:
                    cpt +=1
            totalCpt += cpt

        return totalCpt