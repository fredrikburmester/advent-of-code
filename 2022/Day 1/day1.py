"""
"""
import time
import sys

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=1
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def part1(input_list):
    """ Part 1 """
    total = 0
    largest_total = 0
    for line in input_list:
        if line == '':
            if(total > largest_total):
                largest_total = total
            total = 0
        else:
            total += int(line)


    return largest_total


def part2(input_list):
    """ Part 2 """
    total_sums = []
    total = 0

    for line in input_list:
        if line == '':
            total_sums.append(total)
            total = 0
        else:
            total += int(line)

    total_sums.sort(reverse=True)
    return sum(total_sums[0:3])


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
