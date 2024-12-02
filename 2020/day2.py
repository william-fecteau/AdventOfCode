from utils.aoc_utils import AOCDay

class Day2(AOCDay):
    def common(self):
        # Amélioration possible: Mettre ça dans un dictionnaire?
        self.passwords = []
        self.chars = []
        self.left = []
        self.right = []

        for line in self.inputData:
            policy, char, password = line.split(' ')
            left, right = policy.split('-')
    
            self.passwords.append(password)
            self.left.append(int(left))
            self.right.append(int(right))
            self.chars.append(char[:-1])


    def part1(self):
        cpt = 0
        for i in range(len(self.passwords)):
            occ = self.passwords[i].count(self.chars[i])

            if occ >= self.left[i] and occ <= self.right[i]:
                cpt = cpt + 1

        return cpt
    
    def part2(self):
        cpt = 0
        for i in range(len(self.passwords)):
            password = self.passwords[i]

            if bool(password[self.left[i] - 1] == self.chars[i]) ^ bool(password[self.right[i] - 1] == self.chars[i]):
                cpt = cpt + 1 

        return cpt