"""
"""
import sys
import time

PATH="/Users/fredrikburmester/Documents/GitHub/advent-of-code"
DAY=8
INPUT_PATH=f"{PATH}/2022/Day {DAY}/input.txt"

sys.path.append(PATH)  
from utils.helpers import *


def check_dir(i, j, matrix, part=1, direction='right'):
    values_in_direction = []
    value = matrix[i][j]

    if direction == "right":
        for j in range(j + 1, len(matrix[0])):
            values_in_direction.append(matrix[i][j])
    elif direction == "left":
        for j in range(j - 1, -1, -1):
            values_in_direction.append(matrix[i][j])
    elif direction == "up":
        for i in range(i - 1, -1, -1):
            values_in_direction.append(matrix[i][j])
    elif direction == "down":
        for i in range(i + 1, len(matrix)):
            values_in_direction.append(matrix[i][j])

    if part == 2:
        return count_seen(values_in_direction, value)
    
    for v in values_in_direction:
        if v >= value:
            return 0
    return 1


def count_seen(values, input_value):
    total_seen = 0
    for v in values:
        if v >= input_value:
            total_seen += 1
            return total_seen
        elif v < input_value:
            total_seen += 1
        else:
            return total_seen
    return total_seen


def calculate_scenic_score(i, j, matrix):
    dirs = ['left', 'right', 'up', 'down']
    scores = [check_dir(i, j, matrix, 2, d) for d in dirs]
    
    scenic_score = 1
    for s in scores:
        scenic_score *= s

    return scenic_score


def part1(input_list):
    """ Part 1"""

    seen = 0
    matrix = [[int(x) for x in line] for line in input_list]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            if check_dir(i, j, matrix, 1, 'left') or check_dir(i, j, matrix, 1, 'right') or check_dir(i, j, matrix, 1, 'up') or check_dir(i, j, matrix, 1, 'down'):
                seen += 1
    return seen


def part2(input_list):
    """ Part 2 """
    matrix = [[int(x) for x in line] for line in input_list]
    scenic_score = [calculate_scenic_score(i, j, matrix) for i, line in enumerate(matrix) for j in range(len(line))]
    return max(scenic_score)


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