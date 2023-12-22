import sys
import time
from functools import reduce
from itertools import cycle
from math import gcd

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=8
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


class Node:
    def __init__(self, data: str):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def PrintTree(self):
        print(self.data)


def parse_line(line):
    line = line.split(" = (")
    a = line[0]
    r = line[1].split(", ")
    b = r[0]
    c = r[1].split(")")[0]
    return a, b, c

def get_positions(positions, d, step):
    return [d[pos][0] if step == 'L' else d[pos][1] for pos in positions]

def part1(input_list):
    """ Part 1"""

    end = 'ZZZ'
    pos = 'AAA'
    
    d = dict()

    # Instructions are b or c
    steps = input_list[0]

    for line in input_list[2:]:
        a, b, c = parse_line(line)
        d[a] = (b, c)

    print(steps, len(steps))
    for key, value in d.items():
        print(key, value)

    i = -1
    count = 0
    while True:
        count += 1
        i += 1
        if i >= len(steps):
            i = 0

        step = steps[i]
        if step == 'L':
            pos = d[pos][0]
        else:
            pos = d[pos][1]

        if pos == end:
            return count
        
def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_list(lst):
    return reduce(lcm, lst)

def add_until_equal(numbers):
    differences = [abs(j - i) for i, j in zip(numbers, numbers[1:])]
    lcm_diff = lcm_list(differences)

    max_number = max(numbers)
    # Find how many times to add the lcm_diff to reach a number where all numbers are the same
    steps = max((max_number - num + lcm_diff - 1) // lcm_diff for num in numbers)
    return [num + steps * lcm_diff for num in numbers]

def part2(input_list):
    """ Part 2"""

    d = dict()
    steps = input_list[0]

    for line in input_list[2:]:
        a, b, c = parse_line(line)
        d[a] = (b, c)

    positions = []
    for key, _ in d.items():
        if key[2] == 'A':
            positions.append(key)

    # Check how many steps it takes to reach XXZ for each path.
    # This will result in a list of numbers that represents how many steps it takes for each path to reach XXZ.
    counts = []
    step_cycle = cycle(steps)  
    for _p in positions:
        c = 0
        p = [_p]
        while True:
            c += 1
            step = next(step_cycle)
            p = get_positions(p, d, step)
            if all(pos[2] == 'Z' for pos in p):
                counts.append(c)
                break

    print(counts)

    # Find the lowest common multiple of the numbers in the list.
    # This will be the number of steps it takes for all paths to reach XXZ at the same time.
    return lcm_list(counts)


def main():
    with open(INPUT_PATH, "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    # t0 = time.time()
    # result = part1(input_list)
    # t1 = time.time()
    # print(f"\n{bcolors.OKGREEN}{result}{bcolors.ENDC} is the result of part 1.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()
    print(f"\n{bcolors.OKGREEN}{result2}{bcolors.ENDC} is the result of part 2.\n{bcolors.OKBLUE}{round(t1-t0, 4)}{bcolors.ENDC} seconds\n")


if __name__ == "__main__":
    main()
