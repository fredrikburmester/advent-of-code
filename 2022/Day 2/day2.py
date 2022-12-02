"""
Didn't really think about this one. 
"""
import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=2
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

mapp = {
    'A': 'X', # rock
    'B': 'Y', # paper
    'C': 'Z', # scissors
}

oposite_mapp = {
    'X': 'B',
    'Y': 'C',
    'Z': 'A',
}

rps = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

rps2 = {
    'A': 1,
    'B': 2,
    'C': 3
}


def y_win_point_fn(x,y):
    if x == y: 
        return 3
    elif x == 'X' and y == 'Y':
        return 6
    elif x == 'Y' and y == 'Z':
        return 6
    elif x == 'Z' and y == 'X':
        return 6
    return 0

def part1(input_list):
    """ Part 1"""
    score = 0
    for line in input_list:
        line = [str(x) for x in line.split(" ")]
        p1 = mapp[line[0]]
        p2 = line[1]
        score += rps[p2] + y_win_point_fn(p1, p2)
    return score


def need_to_win(a):
    if a == 'A':
        return 'B'
    elif a == 'B':
        return 'C'
    elif a == 'C':
        return 'A'

def need_to_lose(a):
    if a == 'A':
        return 'C'
    elif a == 'B':
        return 'A'
    elif a == 'C':
        return 'B'

def need_to_draw(a):
    return a


def part2(input_list):
    """ Part 2 """
    score = 0
    for line in input_list:
        line = [str(x) for x in line.split(" ")]
        p1 = line[0]
        nedd_to = line[1]
        if nedd_to == 'X':
            score += 0 + rps2[need_to_lose(p1)]
        elif nedd_to == 'Y':
            score += 3 + rps2[need_to_draw(p1)]
        elif nedd_to == 'Z':
            score += 6 + rps2[need_to_win(p1)]
    return score


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
