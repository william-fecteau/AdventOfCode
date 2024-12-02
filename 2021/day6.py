from utils.aoc_utils import AOCDay
import copy

class Day6(AOCDay):
    def common(self):
        lstFishes = [int(x) for x in self.inputData[0].split(',')]
        
        # Make a list where index represent the number of fish with that timer
        self.currentState = [0] * 9 
        for fish in lstFishes:
            self.currentState[fish] +=  1
            
        return 0


    def simulate(self, state, days):
        for _ in range(days):
            newborns = state.pop(0) # Pop the first element
            state.append(newborns) # Append the first element to the end
            state[6] += newborns # Reset parents to 6
        
        return sum(state)


    def part1(self):
        return self.simulate(self.currentState, 80)


    def part2(self):
        return self.simulate(self.currentState, 256-80)