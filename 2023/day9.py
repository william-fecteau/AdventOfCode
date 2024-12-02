from utils.aoc_utils import AOCDay


class Day9(AOCDay):
    def common(self):
        self.series = [[int(x) for x in line.split()] for line in self.inputData]

    def extrapolate_value(self, serie, is_right):
        current = [serie[i + 1] - serie[i] for i in range(0, len(serie) - 1)]

        if all([x == 0 for x in current]):
            return serie[-1]

        value = self.extrapolate_value(current, is_right)

        return value + serie[-1] if is_right else serie[0] - value

    def part1(self):
        return sum([self.extrapolate_value(serie, True) for serie in self.series])

    def part2(self):
        return sum([self.extrapolate_value(serie, False) for serie in self.series])
