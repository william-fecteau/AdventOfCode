from utils.aoc_utils import AOCDay
import re


class Day1(AOCDay):
    def common(self):
        return 0

    def get_calibration_value(self, line):
        without_letters = re.sub('\D', '', line)
        return int(without_letters[0] + without_letters[-1])

    def replace_text_digit(self, line):
        replace_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        for key, value in replace_dict.items():
            for i in range(len(line)):
                if line[i:].startswith(key):
                    line = line.replace(key, value)

        return self.get_calibration_value(line)

    def part1(self):
        return sum([self.get_calibration_value(x) for x in self.inputData])

    def part2(self):
        return sum([self.replace_text_digit(x) for x in self.inputData])
