"""
<3 python for this one
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=3
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part1(input_list):
    """ Part 1"""

    total = 0

    for line in input_list:
        line = [str(x) for x in line]

        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]

        matching = [x for x in first_half if x in second_half]

        if len(matching) > 0:
            l = matching[0]
            if l in letters:
                index = letters.index(l) + 1
                total += index
                continue
            if l in capital_letters:
                index_2 = capital_letters.index(l) + 27
                total += index_2
                continue

    return total


def part2(input_list):
    """ Part 2 """

    total = 0

    # every third line
    for i in range(0, len(input_list), 3):

        line = [str(x) for x in input_list[i]]
        line_2 = [str(x) for x in input_list[i+1]]
        line_3 = [str(x) for x in input_list[i+2]]

        matching = [x for x in line if x in line_2 and x in line_3]

        if len(matching) > 0:
            l = matching[0]
            if l in letters:
                index = letters.index(l) + 1
                total += index
                continue
            if l in capital_letters:
                index_2 = capital_letters.index(l) + 27
                total += index_2
                continue

    return total


def main():
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

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
