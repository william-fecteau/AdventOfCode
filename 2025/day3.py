from utils.aoc_utils import AOCDay

class Day3(AOCDay):
    def common(self):
        pass

    def get_bank_joltage(self, bank: str, nb_digits: int):
        digits = [int(str_d) for str_d in bank]

        str_joltage = ""
        for _ in range(nb_digits):
            rest = nb_digits-len(str_joltage)-1
            
            if rest == 0:
                pool = digits[:]
            else:
                pool = digits[:-(rest)]

            max_digit = max(pool)
            max_digit_index = digits.index(max_digit)


            digits = digits[max_digit_index+1:]

            str_joltage += str(max_digit)
        
        return int(str_joltage)

    def part1(self):
        total = 0
        for bank in self.inputData:
            total += self.get_bank_joltage(bank, 2)
        
        return total


    def part2(self):
        total = 0
        for bank in self.inputData:
            total += self.get_bank_joltage(bank, 12)
        
        return total
