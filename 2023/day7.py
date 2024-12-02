from dataclasses import dataclass
from enum import Enum
from utils.aoc_utils import AOCDay


@dataclass
class Hand():
    cards: str
    bid: int


class Day7(AOCDay):
    def common(self):
        self.hands = [Hand(line.split(' ')[0], int(
            line.split(' ')[1])) for line in self.inputData]

        self.FIVE_OF_A_KIND = 0
        self.FOUR_OF_A_KIND = 1
        self.FULL_HOUSE = 2
        self.THREE_OF_A_KIND = 3
        self.TWO_PAIRS = 4
        self.PAIR = 5
        self.HIGH_CARD = 6

    def get_hand_type(self, hand: Hand, is_part_two: bool) -> int:
        card_count = sorted([hand.cards.count(card)
                             for card in set(hand.cards)], reverse=True)

        nb_j = hand.cards.count('J')
        # If the highest card card is not 'J'
        if is_part_two and 1 <= nb_j < card_count[0]:
            card_count[0] += nb_j
            card_count.remove(nb_j)
        # If the highest card card is 'J' and we do not have only 'JJJJJ'
        elif is_part_two and len(card_count) > 1 and nb_j == card_count[0]:
            card_count[1] += nb_j
            card_count.remove(nb_j)

        if 5 in card_count:
            return self.FIVE_OF_A_KIND
        elif 4 in card_count:
            return self.FOUR_OF_A_KIND
        elif 3 in card_count and 2 in card_count:
            return self.FULL_HOUSE
        elif 3 in card_count:
            return self.THREE_OF_A_KIND
        elif card_count.count(2) == 2:
            return self.TWO_PAIRS
        elif 2 in card_count:
            return self.PAIR
        else:
            return self.HIGH_CARD

    def tie_breaker(self, hands: list[Hand], value_dict: dict[str, str]) -> list[Hand]:
        for hand in hands:
            hand.cards = "".join([value_dict[card] for card in hand.cards])

        result = sorted(hands, key=lambda hand: hand.cards, reverse=True)

        inv_dict = {v: k for k, v in value_dict.items()}
        for hand in result:
            hand.cards = "".join([inv_dict[card] for card in hand.cards])

        return result

    def count_winnings(self, hands_by_types: list[list[Hand]], value_dict: dict[str, str]):
        current_rank = len(self.hands)
        total_winnings = 0
        for hand_by_type in hands_by_types:
            sorted_hands = self.tie_breaker(hand_by_type, value_dict)

            for hand in sorted_hands:
                total_winnings += hand.bid * current_rank
                current_rank -= 1

        return total_winnings

    def part1(self):
        hands_by_types: list[list[Hand]] = [[] for _ in range(7)]
        for hand in self.hands:
            hand_type = self.get_hand_type(hand, False)
            hands_by_types[hand_type].append(hand)

        value_dict = {
            '2': 'a',
            '3': 'b',
            '4': 'c',
            '5': 'd',
            '6': 'e',
            '7': 'f',
            '8': 'g',
            '9': 'h',
            'T': 'i',
            'J': 'j',
            'Q': 'k',
            'K': 'l',
            'A': 'm'
        }
        return self.count_winnings(hands_by_types, value_dict)

    def part2(self):
        hands_by_types: list[list[Hand]] = [[] for _ in range(7)]
        for hand in self.hands:
            hand_type = self.get_hand_type(hand, True)
            hands_by_types[hand_type].append(hand)

        value_dict = {
            'J': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            'T': 'j',
            'Q': 'k',
            'K': 'l',
            'A': 'm'
        }
        return self.count_winnings(hands_by_types, value_dict)
