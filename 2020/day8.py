from utils.aoc_utils import AOCDay

class Day8(AOCDay):
    def common(self):
        self.op = {"acc": self.inc, "jmp": self.jmp, "nop": self.nop}

    def inc(self, num):
        self.acc += num
        self.pointer += 1

    def jmp(self, num):
        self.pointer += num

    def nop(self, num):
        self.pointer += 1

    
    def runCode(self, lines):
        self.acc = 0
        self.pointer = 0
        self.executedLines = set()

        terminated = False

        while self.pointer not in self.executedLines:
            if(self.pointer >= len(lines)):
                terminated = True
                break

            line = lines[self.pointer]
            opLine, paramLine = line.split(' ')

            sign = 1
            if paramLine[0] == '-':
                sign = -1
            paramLine = sign * int(paramLine[1:])

            self.executedLines.add(self.pointer)

            self.op[opLine](paramLine)
        
        return terminated


    def part1(self):
        lines = self.inputData

        self.runCode(lines)

        return self.acc

    def part2(self):
        terminated = False

        for i in range(len(self.inputData)):
            lines = self.inputData.copy()

            if lines[i][:3] == "nop":
                lines[i] = lines[i].replace('nop', 'jmp')
            elif lines[i][:3] == 'jmp':
                lines[i] = lines[i].replace('jmp', 'nop')
            
            if self.runCode(lines):
                break

        return self.acc