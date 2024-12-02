from utils.aoc_utils import AOCDay

class Day2(AOCDay):
    def common(self):
        # Putting input in this form (firstLetterOfCommand, units)
        self.commands = [(cmd.split(' ')[0][0], int(cmd.split(' ')[1])) for cmd in self.inputData]
        
    def part1(self):
        (x, depth) = (0, 0)
                        
        for cmdTuple in self.commands:
            cmdCode, units = cmdTuple
            
            if cmdCode == 'f':
                x+=units
            elif cmdCode == 'd':
                depth+=units
            elif cmdCode == 'u':
                depth-=units
            
        return x * depth
    
    def part2(self):
        (x, depth, aim) = (0, 0, 0)
        
        for cmdTuple in self.commands:
            cmdCode, units = cmdTuple
            
            if cmdCode == 'f':
                x+=units
                depth+=(aim*units)
            elif cmdCode == 'd':
                aim+=units
            elif cmdCode == 'u':
                aim-=units
        
        return x * depth