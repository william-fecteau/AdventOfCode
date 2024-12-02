from utils.aoc_utils import AOCDay

class Day1(AOCDay):
    def part1(self):
        self.inputData.sort(key = int)

        for i in self.inputData:
            for j in self.inputData:
                if i == j:
                    break

                sum = int(i) + int(j)

                if(sum == 2020):
                    return int(i) * int(j)
                    
                    break
                elif(sum > 2020):
                    break

        return -1
    
    def part2(self):
        self.inputData.sort(key = int)

        for i in self.inputData:
            for j in self.inputData:
                if i == j:
                    break
                elif int(i) + int(j) > 2020:
                    break

                for k in self.inputData:
                    if i == k:
                        break
                    
                    sum = int(i) + int(j) + int(k)

                    if(sum == 2020):
                        return int(i) * int(j) * int(k)
                    elif(sum > 2020):
                        break

        return -1