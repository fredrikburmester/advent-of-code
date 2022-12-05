"""
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=5
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def part1(input_list):
    """ Part 1"""

    l = [[] for _ in range(9)]

    for line in input_list[0:8]:
        for i in range(0, 4*9, 4):
            if line[i+1] != " ":
                l[i//4].append(line[i+1])

    for line in l:
        line.reverse()

    for line in input_list[10:]:
        line = [x for x in line.split(" ")]

        amount = int(line[1])
        _from = int(line[3]) - 1
        _to = int(line[5]) - 1

        for i in range(amount):
            l[_to].append(l[_from].pop())

    result = ""
    for i in range(9):
        result += l[i][-1]

    return result


def part2(input_list):
    """ Part 2 """
    l = [[] for _ in range(9)]

    for line in input_list[0:8]:
        for i in range(0, 4*9, 4):
            if line[i+1] != " ":
                l[i//4].append(line[i+1])

    for line in l:
        line.reverse()

    for line in input_list[10:]:
        line = [x for x in line.split(" ")]

        amount = int(line[1])
        _from = int(line[3]) - 1
        _to = int(line[5]) - 1

        t = l[_from][-amount:]
        l[_from] = l[_from][:-amount]
        l[_to].extend(t)
    
    result = ""
    for i in range(9):
        result += l[i][-1]

    return result


def main():
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [line for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


if __name__ == "__main__":
    main()
