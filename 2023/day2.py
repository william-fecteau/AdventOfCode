from dataclasses import dataclass
from utils.aoc_utils import AOCDay
import re


@dataclass
class GameSet:
    nb_blue: int
    nb_red: int
    nb_green: int


@dataclass
class Game:
    sets: list[GameSet]


class Day2(AOCDay):
    def common(self):
        self.games = []
        for line in self.inputData:
            current_game = Game([])
            _, rest = line.split(':')

            for set in rest.split(';'):
                current_set = GameSet(0, 0, 0)

                for color in set.replace(' ', '').split(','):
                    nb = int(re.sub('\D', '', color))
                    if 'red' in color:
                        current_set.nb_red += nb
                    elif 'blue' in color:
                        current_set.nb_blue += nb
                    elif 'green' in color:
                        current_set.nb_green += nb

                current_game.sets.append(current_set)

            self.games.append(current_game)

        return 0

    def part1(self):
        NB_RED = 12
        NB_GREEN = 13
        NB_BLUE = 14

        game_id_sum = 0
        for i, game in enumerate(self.games):
            if all(x.nb_blue <= NB_BLUE and x.nb_red <= NB_RED and x.nb_green <= NB_GREEN for x in game.sets):
                game_id_sum += i + 1

        return game_id_sum

    def part2(self):
        power_sum = 0
        for i, game in enumerate(self.games):
            max_red = max([x.nb_red for x in game.sets])
            max_green = max([x.nb_green for x in game.sets])
            max_blue = max([x.nb_blue for x in game.sets])

            power_sum += max_red * max_green * max_blue

        return power_sum
