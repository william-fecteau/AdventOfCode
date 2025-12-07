from utils.aoc_utils import AOCDay

class Day5(AOCDay):
    def common(self):
        # Fresh ingredients
        self.fresh_ingredients_ranges = []
        i = 0
        line = self.inputData[i]
        while len(line) > 0:
            lower, upper = line.split("-")
            lower = int(lower)
            upper = int(upper)

            self.fresh_ingredients_ranges.append(range(lower, upper+1))
            line = self.inputData[i]
            i += 1
        
        self.fresh_ingredients_ranges = list(set(self.fresh_ingredients_ranges))

        # Available ingredients
        self.available_ingredients = []
        while i < len(self.inputData):
            line = self.inputData[i]
            self.available_ingredients.append(int(line))

            i += 1
        
    def part1(self):
        count = 0
        for ing in self.available_ingredients:
            for a_range in self.fresh_ingredients_ranges:
                if ing in a_range:
                    count += 1
                    break
        
        return count

    def is_overlapping(self, range_1, range_2):
        return max(range_1.start, range_2.start) < min(range_1.stop, range_2.stop)

    def part2(self):
        # Merge all overlapping ranges
        valid_ranges = []

        for a_range in self.fresh_ingredients_ranges:
            # Keep merging until no more overlaps with this range
            merged_range = a_range
            changed = True
            
            while changed:
                changed = False
                ranges_to_remove = []
                
                for b_range in valid_ranges:
                    if self.is_overlapping(merged_range, b_range):
                        start = min(merged_range.start, b_range.start)
                        end = max(merged_range.stop, b_range.stop)
                        merged_range = range(start, end)
                        ranges_to_remove.append(b_range)
                        changed = True
                
                # Remove all ranges that were merged
                for r in ranges_to_remove:
                    valid_ranges.remove(r)
            
            valid_ranges.append(merged_range)
        
        return sum([len(r) for r in valid_ranges])
            