"""
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=10
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def is_40(value):
    # return True is divisible by 40
    # 20, 60, 100... 
    return (value-20) % 40 == 0


assert is_40(20)
assert is_40(60)
assert is_40(100)
assert not is_40(40)


def part1(input_list):
    """ Part 1"""

    mapp = defaultdict(int)
    s = set()

    # Get first line
    first = input_list[0]

    # Size of matrix, ie first line (column) and all rows
    lx = len(first)
    ly = len(input_list)

    X = 1
    cycles = 0
    total = 0
    for line in input_list:
        if line.startswith('noop'):
            cycles += 1
        else:
            instruction, value_str = line.split(' ')
            value = int(value_str)

            if instruction == 'addx':
                cycles += 1
                if is_40(cycles):
                    print(f"Cycle {cycles}, X: {X} = {cycles * X}")
                    total += cycles * X
                
                cycles += 1
                
                if is_40(cycles):
                    print(f"Cycle {cycles}, X: {X} = {cycles * X}")
                    total += cycles * X
                

                X += value

    return total


def part2(input_list):
    """ Part 2 """
    crt = ['.' for _ in range(0, 240)]
    X = 1
    cycle = 0

    for line in input_list:
        if line.startswith('noop'):
            if (cycle % 40) in [X - 1, X, X + 1]:
                crt[cycle] = '#'
            cycle += 1
            if (cycle % 40) in [X - 1, X, X + 1]:
                crt[cycle] = '#'
        else:
            _, value_str = line.split()
            value = int(value_str)
            if (cycle % 40) in [X - 1, X, X + 1]:
                crt[cycle] = '#'
            cycle += 1
            if (cycle % 40) in [X - 1, X, X + 1]:
                crt[cycle] = '#'
            cycle += 1
            X += value

    for i in range(1, len(crt)+1):
        print(crt[i-1], end="")
        if i % 40 == 0:
            print()
    
    return 0


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
