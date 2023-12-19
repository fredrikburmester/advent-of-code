import sys
import time
import math
import pathlib
from collections import defaultdict, Counter, deque
from copy import deepcopy

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=2
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *

def part1(input_list):
    """ Part 1"""

    max_red = 12
    max_green = 13
    max_blue = 14
    
    def is_ok(turn, amount):
        if "green" in turn:
            if amount > max_green:
                return False
        elif "red" in turn:
            if amount > max_red:
                return False
        elif "blue" in turn:
            if amount > max_blue:
                return False
        return True

    def is_ok_game(rounds, index):
        for r in rounds:
            option = r.split(", ")
            for _set in option:
                amount = int(_set.split(" ")[0])
                if not is_ok(_set, amount):
                    return 0
        return index

    s = 0
    for line in input_list:
        index = int(line.split("Game ")[1].split(":")[0])
        rounds = line.split(": ")[1].split("; ")
        s += is_ok_game(rounds, index)
    return s


def part2(input_list):
    """ Part 2 """

    s = 0
    for line in input_list:
        max_red = 0
        max_green = 0
        max_blue = 0

        rounds = line.split(": ")[1].split("; ")

        for r in rounds:
            option = r.split(", ")
            for _set in option:
                amount = int(_set.split(" ")[0])
                if "green" in _set and amount > max_green:
                    max_green = amount
                elif "blue" in _set and amount > max_blue:
                    max_blue = amount
                elif "red" in _set and amount > max_red:
                    max_red = amount

        _power = max_red * max_green * max_blue
        s += _power

    return s

def read_input(file_path):
    with open(file_path, "r", encoding='UTF-8') as file:
        return [line.strip() for line in file]

def time_execution(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, round(end_time - start_time, 4)

def main():
    input_list = read_input(INPUT_PATH)

    result1, time1 = time_execution(part1, input_list)
    print(f"\n{bcolors.OKGREEN}{result1}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{time1}{bcolors.ENDC} seconds\n")

    result2, time2 = time_execution(part2, input_list)
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{time2}{bcolors.ENDC} seconds\n")

if __name__ == "__main__":
    main()
