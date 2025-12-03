from utils.aoc_utils import AOCDay

class Day2(AOCDay):
    def common(self):
        self.ranges = []
        for str_range in self.rawData.split(","):
            left, right = str_range.split("-")

            self.ranges.append(list(range(int(left), int(right)+1)))

        return 0

    def is_invalid_id(self, sequence: str):
        # A sequence of 1 or less i not repeating
        if len(sequence) == 0 or len(sequence) % 2 != 0:
            return False
        
        # If even, must be a repetition
        middle = len(sequence) // 2
        for i, c in enumerate(sequence[:middle]):
            if c != sequence[middle+i]:
                return False
        
        return True

    def is_invalid_id_p2(self, sequence: str):
        middle = len(sequence) // 2
        for subsequence_size in range(1, middle+1):
            if len(sequence) % subsequence_size != 0:
                continue

            n_subsequences = len(sequence) // subsequence_size

            subsequence = sequence[:subsequence_size]
            if subsequence * n_subsequences == sequence:
                return True
        
        return False

    def part1(self):
        total = 0
        for rangee in self.ranges:
            for val in rangee:
                if self.is_invalid_id(str(val)):
                    total += val

        return total

    def part2(self):
        total = 0
        for rangee in self.ranges:
            for val in rangee:
                if self.is_invalid_id_p2(str(val)):
                    total += val

        return total
