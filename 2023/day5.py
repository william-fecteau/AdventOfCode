from dataclasses import dataclass
from utils.aoc_utils import AOCDay
import re


@dataclass
class Map:
    source_range: range
    destination_range: range


@dataclass
class Section:
    maps: list[Map]


class Day5(AOCDay):
    def common(self):
        self.seeds = [int(x) for x in re.search(r'seeds: ([\d ]+)',
                                                self.rawData).group(1).split()]
        self.sections: list[Section] = []

        for reg_match in re.finditer(r'.+-to-.+ map:\n(([\d ]+\n)+)', self.rawData):
            maps: list[Map] = []

            for entry in reg_match.group(1).splitlines():
                destination_start, source_start, range_length = [
                    int(x) for x in entry.split()]
                source_range = range(
                    source_start, source_start + range_length - 1)
                destination_range = range(
                    destination_start, destination_start + range_length - 1)

                maps.append(
                    Map(source_range, destination_range))

            self.sections.append(Section(maps))

    def find_location_for_seed(self, seed: int) -> int:
        current = seed
        for section in self.sections:
            for map in section.maps:
                if map.source_range.start <= current <= map.source_range.stop:
                    current = map.destination_range.start + \
                        (current - map.source_range.start)
                    break

        return current

    def part1(self):
        return min(self.find_location_for_seed(seed) for seed in self.seeds)

    def get_range_intersection(self, range1: range, range2: range) -> range | None:
        start = max(range1.start, range2.start)
        end = min(range1.stop, range2.stop)

        if start <= end:
            return range(start, end)
        else:
            return None

    def part2(self):
        _, rest = self.inputData[0].split(': ')
        str_nb = rest.split(' ')
        seed_ranges = [range(int(x1), int(x1) + int(x2) - 1)
                       for x1, x2 in zip(str_nb[::2], str_nb[1::2])]

        range_queue: list[range] = seed_ranges
        for section in self.sections:
            next_ranges: list[range] = []

            while len(range_queue) > 0:
                current_range: range = range_queue.pop(0)
                for map in section.maps:
                    intersection = self.get_range_intersection(
                        current_range, map.source_range)

                    # Intersection found
                    if intersection is not None:
                        next_ranges.append(range(intersection.start - map.source_range.start + map.destination_range.start,
                                                 intersection.stop - map.source_range.start + map.destination_range.start))

                        # If intersection is not spanning the whole source range, add remaining ranges to queue
                        if intersection.start > current_range.start:
                            range_queue.append(
                                range(current_range.start, intersection.start - 1))
                        elif intersection.stop < current_range.stop:
                            range_queue.append(
                                range(intersection.stop + 1, current_range.stop))

                        break
                # We did not find any intersection, add the current range without modification
                else:
                    next_ranges.append(current_range)

            range_queue = next_ranges

        return min(x.start for x in range_queue)
