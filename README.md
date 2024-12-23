# My Advent Of Code solutions 

## What is Advent Of Code?
Advent of code is a series of coding challenges in the form of an advent calendar : One challenge divided in two parts per day from December 1rst up until December 25th [https://adventofcode.com/](https://adventofcode.com/)

## Framework
This repo is a fork of my AoC framework to handle the inputs and execution for each year
- [https://github.com/william-fecteau/AdventOfCodePythonFramework](https://github.com/william-fecteau/AdventOfCodePythonFramework)

## Installation
1. Clone the repo
2. Install the requirements ```pip install -r requirements.txt```
3. Create a ```.env``` file at the root of the repo
4. In this ```.env``` file, add the two following variables and change their values for your need :
```
AOC_SESSION_COOKIE=yourSessionCookie
AOC_YEAR=2021
```
*Note: You can get your session cookie by logging to the AoC website and looking in the cookies of one of your requests using dev tools. This cookie will be needed to download your input automatically*

## Framework flow
A day file is created with this template :
```
from utils.aoc_utils import AOCDay

class DayTemplate(AOCDay):
    def common(self):
        #print(self.inputData)
        #print(self.rawData)
        return 0

    def part1(self):
        return 0
    
    def part2(self):
        return 0
```
*Note: ```self.inputData``` contains the list of every line from your input (Splitted on '\n') and ```self.rawData``` contains all the data in a single string (Including all the '\n')*


## How to use it
### Start a day
To start a day, use this command : ```python main.py <dayNumber>```


If its not already there, this will create your day file for you to program in.


Your day file will be in ```./<year>/day<dayNumber>.py``` (This is where you program!)

### Run a day
To run a day, use this command : ```python main.py <dayNumber>``` (Notice it's the same command as how to start a day)


The input file will be downloaded in ```./<year>/inputs/day<dayNumber>.txt``` (Normally you don't need to touch this file! It will be parsed automatically)


After downloading the input, it will run your code and produce the output in the console and at ```./<year>/outputs/day<dayNumber>.txt```
