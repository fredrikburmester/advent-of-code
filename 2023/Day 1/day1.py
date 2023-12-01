import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=1
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "zero"
]

def value_of_number(number):
    return numbers.index(number) + 1

def part1(input_list):
    """ Part 1"""
    res = 0

    for line in input_list:
        line = [int(x) for x in line if x.isdigit()]

        if len(line) == 0:
            continue
        res += int(f"{line[0]}{line[-1]}")

    return res

def part2(input_list):
    """ Part 2 """
    res = 0

    for line in input_list:
        first = ""
        last = ""

        found_first = False
        for i, l1 in enumerate(line):
            if found_first:
                break
            temp = l1

            if l1.isdigit():
                first = str(l1)
                break

            for j in range(i+1, len(line)):
                if first != "":
                    found_first = True

                l2 = line[j]
                temp += l2

                if temp in numbers:
                    first = str(value_of_number(temp))
                    break

        for i, l1 in enumerate(line):
            temp = l1

            if l1.isdigit():
                last = str(l1)

            for j in range(i+1, len(line)):
                l2 = line[j]
                temp += l2
                if temp in numbers:
                    last = str(value_of_number(temp))
                    break

        res += int(f"{first}{last}")

    return res

def main():
    try:
        with open(INPUT_PATH, "r", encoding='UTF-8') as file:
            input_list = [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File not found: {INPUT_PATH}")
        sys.exit(1)

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
