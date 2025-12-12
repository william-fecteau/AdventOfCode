import networkx as nx
from utils.aoc_utils import AOCDay

class Day11(AOCDay):
    def common(self):
        self.G = nx.DiGraph()
        for line in self.inputData:
            node = line[0:3]
            splitted = line.split(" ")
            edges = splitted[1:]
            self.G.add_edges_from([(node, e) for e in edges])

    def dfs(self, current, end, visited, history):
        if current == end:
            return 1
        if current in history:
            return history[current]

        count = 0
        for n in self.G.neighbors(current):
            count += self.dfs(n, end, visited, history)

        history[current] = count

        return count
        
    def part1(self):
        return self.dfs("you", "out", set(), {})

    def part2(self):
        # svr -> fft -> dac -> out
        count1 = self.dfs("svr", "fft", set(), {}) * self.dfs("fft", "dac", set(), {}) * self.dfs("dac", "out", set(), {})
        
        # svr -> dac -> fft -> out
        count2 = self.dfs("svr", "dac", set(), {}) * self.dfs("dac", "fft", set(), {}) * self.dfs("fft", "out", set(), {})
        
        return count1 + count2
            
