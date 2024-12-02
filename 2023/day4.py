from dataclasses import dataclass
from utils.aoc_utils import AOCDay
import re


@dataclass
class Card:
    winning_numbers: list[int]
    your_numbers: list[int]
    nb_copy: int


class Day4(AOCDay):
    def common(self):
        self.cards: list[Card] = []

        regex = re.compile(r'Card +\d+: ([ \d]+) \| ([ \d]+)')

        for line in self.inputData:
            match = re.search(regex, line)

            winnings = [int(x) for x in match.group(1).split()]
            yours = [int(x) for x in match.group(2).split()]

            self.cards.append(Card(winnings, yours, 1))

    def get_nb_points(self, card_index: int, card: Card) -> int:
        nb_match = sum(
            1 for nb in card.winning_numbers if nb in card.your_numbers)
        if nb_match == 0:
            return 0

        for j in range(1, nb_match + 1):
            self.cards[card_index + j].nb_copy += card.nb_copy

        return 2 ** (nb_match - 1)

    def part1(self):
        return sum([self.get_nb_points(i, card) for i, card in enumerate(self.cards)])

    def part2(self):
        return sum([card.nb_copy for card in self.cards])
