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
    """ 
    Part 1
    
    Expect lines are never empty and always contain at least two numbers.
    """
    
    res = 0

    for line in input_list:
        line = [str(x) for x in line if x.isdigit()]
        res += int(line[0] + line[-1])
    return res


# def part2(input_list):
#     """ Part 2 """
#     res = 0

#     for line in input_list:
#         first = ""
#         last = ""

#         # Find first number
#         found_first = False
#         for i, l1 in enumerate(line):
#             if found_first:
#                 break
#             temp = l1

#             if l1.isdigit():
#                 first = str(l1)
#                 break

#             for j in range(i+1, len(line)):
#                 if first != "":
#                     found_first = True

#                 l2 = line[j]
#                 temp += l2

#                 if temp in numbers:
#                     first = str(value_of_number(temp))
#                     break

#         # Find last number
#         for i, l1 in enumerate(line):
#             temp = l1

#             if l1.isdigit():
#                 last = str(l1)

#             for j in range(i+1, len(line)):
#                 l2 = line[j]
#                 temp += l2
#                 if temp in numbers:
#                     last = str(value_of_number(temp))
#                     break

#         res += int(f"{first}{last}")

#     return res

def part_2_better(input_list):
    res = 0 
    for line in input_list:
        d = []
        for i, l in enumerate(line):
            if l.isdigit():
                d.append(l)
            for j, num in enumerate(numbers):
                if line[i:].startswith(num):
                    d.append(j+1)
        res += int(f"{d[0]}{d[-1]}")
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

    # t0 = time.time()
    # result2 = part2(input_list)
    # t1 = time.time()
    # print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")
    
    t0 = time.time()
    result2 = part_2_better(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2 better.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

if __name__ == "__main__":
    main()
