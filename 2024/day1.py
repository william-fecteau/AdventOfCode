from utils.aoc_utils import AOCDay

class Day1(AOCDay):
    def common(self):
        self.left_list = []
        self.right_list = []
        for line in self.inputData:
            left, right = line.split("   ")

            self.left_list.append(int(left))
            self.right_list.append(int(right))

    def part1(self):
        self.left_list.sort()
        self.right_list.sort()

        return sum([abs(left - right) for left, right in zip(self.left_list, self.right_list)])

    def part2(self):
        return sum([abs(left * self.right_list.count(left)) for left in self.left_list])
