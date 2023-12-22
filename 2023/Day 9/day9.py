import sys
import time

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=9
INPUT_PATH=f"{PATH}/2023/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def combine(line, d): 
    if all(x == 0 for x in line):
        return 0

    diff = [0]
    for i in range(1, len(line)-1):
        a = line[i]
        b = line[i+1]
        diff.append(b-a)
    return diff[-1] + combine(diff, d+1)

def part1(input_list):
    """ Part 1"""

    results = []
    for line in input_list:
        line = [int(x) for x in line.split(" ") if x != ""]
        line = [0] + line
        results.append(combine(line, 0) + line[-1])

    return sum(results)

def part2(input_list):
    """ Part 2 """

    results = []
    for line in input_list:
        line = [int(x) for x in line.split(" ") if x != ""]
        line = [0] + line[::-1]
        results.append(combine(line, 0) + line[-1])

    return sum(results)


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
