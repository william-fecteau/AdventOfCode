from utils.aoc_utils import AOCDay
import re

class Day4(AOCDay):
    def common(self):
        passports = []
        strPassport = ""

        for line in self.inputData:
            if line != "":
                strPassport += line + " "
            else:
                keyVal = strPassport.split(' ')
                dic = self.convertKeyValToDic(keyVal)
                
                # S'il est valide
                if len(dic) == 7:
                    passports.append(dic)
                strPassport = ""

        # Pour la dernière ligne, qui n'est pas séparé par un ""    
        keyVal = strPassport.split(' ')
        passports.append(self.convertKeyValToDic(keyVal))
            
        self.inputData = passports

    def convertKeyValToDic(self, values):
        dicPassport = {}
        for value in values:
            if(value != ""):
                key, val = value.split(':')

                # On ignore "cid"
                if key != "cid":
                    dicPassport[key] = val

        return dicPassport

    def part1(self):
        return len(self.inputData)
    

    def part2(self):
        validCpt = 0

        for passport in self.inputData:
            valid = True

            validEcl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

            for key in passport:
                val = passport[key]

                if key == "byr":
                    if len(val) != 4:
                        valid = False
                    elif int(val) < 1920 or int(val) > 2002:
                        valid = False
                elif key == "iyr":
                    if len(val) != 4:
                        valid = False
                    elif int(val) < 2010 or int(val) > 2020:
                        valid = False
                elif key == "eyr":
                    if len(val) != 4:
                        valid = False
                    elif int(val) < 2020 or int(val) > 2030:
                        valid = False
                elif key == "hgt":
                    if "cm" in val:
                        val = val[:-2]
                        if int(val) < 150 or int(val) > 193:
                            valid = False
                    elif "in" in val:
                        val = val[:-2]
                        if int(val) < 59 or int(val) > 76:
                            valid = False
                    else:
                        valid = False
                elif key == "hcl":
                    if not re.search("^#[0-9a-f]{6}$", val):
                        valid = False
                elif key == "ecl":
                    if val not in validEcl:
                        valid = False
                elif key == "pid":
                    if not re.search("^[0-9]{9}$", val):
                        valid = False

            if valid:
                validCpt += 1

        return validCpt