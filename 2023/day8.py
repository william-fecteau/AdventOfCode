from dataclasses import dataclass
import math
from utils.aoc_utils import AOCDay
import re


@dataclass
class Node:
    name: str
    left: any
    right: any


class Day8(AOCDay):
    def common(self):
        self.instructions = self.inputData[0]

        self.nodes: dict[str, Node] = {}
        for line in self.inputData[2:]:
            match = re.search(r'(.+) = \((.+), (.+)\)', line)
            current_name, l_name, r_name = match.groups()

            if l_name not in self.nodes:
                self.nodes[l_name] = Node(l_name, None, None)
            if r_name not in self.nodes:
                self.nodes[r_name] = Node(r_name, None, None)
            if current_name not in self.nodes:
                self.nodes[current_name] = Node(current_name, None, None)

            self.nodes[current_name].left = self.nodes[l_name]
            self.nodes[current_name].right = self.nodes[r_name]

    def part1(self):
        current_node = self.nodes["AAA"]
        nb_steps = 0
        while current_node.name != "ZZZ":
            current_instruction = self.instructions[nb_steps % len(
                self.instructions)]

            current_node = current_node.left if current_instruction == "L" else current_node.right

            nb_steps += 1

        return nb_steps

    def part2(self):
        # I noticed that each node that ends with A only has one path to a node with Z and it always repeats the same pattern

        nodes = [node for node in self.nodes.values()
                 if node.name.endswith("A")]

        nb_steps_needed = []

        for node in nodes:
            nb_steps = 0
            current_node = node
            while not current_node.name.endswith("Z"):
                current_instruction = self.instructions[nb_steps % len(
                    self.instructions)]

                current_node = current_node.left if current_instruction == "L" else current_node.right

                nb_steps += 1
            nb_steps_needed.append(nb_steps)

        return math.lcm(*nb_steps_needed)
