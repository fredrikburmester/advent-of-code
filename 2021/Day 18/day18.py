"""
"""
from collections import defaultdict
from copy import deepcopy
import time
import itertools


def split(line: str):
    number = ''
    start = 0
    end = 0
    for i in range(len(line)):
        if line[i].isdigit() and line[i+1].isdigit():
            number = int(line[i] + line[i+1])
            if int(number) >= 10:
                start = i
                end = i+1
                line = line[:start] + "[" + str(int(number) // 2) + "," + str((int(number) + 1) // 2) + "]" + line[end+1:]
                return line

    return line


def reduce(line: str) -> str:
    reduced_line = line
    prev_line = ''
    assert len(line) > 0
    while True:
        # Try to explode
        reduced_line = explode(reduced_line)
        if prev_line != reduced_line:
            prev_line = reduced_line
            continue

        # Try to split
        reduced_line = split(reduced_line)
        if prev_line != reduced_line:
            prev_line = reduced_line
            continue
        else:
            break

    return reduced_line


def explode(line: str) -> str:
    """ Reduce line """
    # Go through all characters and check if depth is equal to 5
    depth = 0
    reduced_line = line
    counter = 0
    counter += 1
    for i, c in enumerate(reduced_line):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        if depth == 5:
            if not reduced_line[i+1].isdigit():
                continue

            n = i
            is_pair = False
            while True:
                n += 1
                if reduced_line[n] == "[":
                    break
                if reduced_line[n] == "]":
                    is_pair = True
                    break

            if not is_pair:
                break

            # Explde
            string = reduced_line[i+1:n]
            x, y = string.split(",")
            reduced_line = reduced_line[:i] + "0" + reduced_line[n+1:]
            reduced_line = add_to_left(reduced_line, int(x), i)
            reduced_line = add_to_right(reduced_line, int(y), i+1)
            return reduced_line
    return reduced_line


def add_to_left(line: str, num: int, i: int) -> str:
    number = ''
    end = 0
    start = 0
    while i > 0:
        i -= 1
        if line[i].isdigit():
            start = i
            end = i
            number = str(line[i]) + str(number)
            if line[i-1].isdigit():
                number = str(line[i-1]) + str(number)
                start = i-1
                break
            break

    if len(number) > 0:
        number = int(number) + int(num)
        line = line[:start] + str(number) + line[end+1:]
    return line


def add_to_right(line: str, num: int, i: int) -> str:
    number = ''
    end = 0
    start = 0
    while i < len(line) - 1:
        i += 1
        if line[i].isdigit():

            start = i
            end = i
            number = str(line[i])
            if line[i+1].isdigit():
                number = str(number) + str(line[i+1])
                end = i+1
                break
            break

    if len(number) > 0:
        number = int(number) + int(num)
        line = line[:start] + str(number) + line[end+1:]
    return line


def magnitude(line: list):
    counter = 0
    while len(line) > 4:
        counter += 1
        if counter > 100:
            return
        for i in range(len(line)):
            if line[i].isdigit() and line[i + 2].isdigit():
                start = i - 1
                end = i + 4
                # Explode
                x = int(line[i])
                y = int(line[i + 2])
                pair_sum = 3 * x + 2 * y
                line = line[:start] + [str(pair_sum)] + line[end:]
                break
    return line


def part1(input_list):
    """ Part 1"""
    reduced_line = ''
    for i, line in enumerate(input_list):
        # 1. Read line
        line = [str(x) for x in line]
        # 2. Convert list to string
        line = ''.join(line)
        # 3. Add previous line
        if i != 0:
            line = "[" + reduced_line + "," + line + "]"
        # 3. Reduce line
        reduced_line = reduce(line)

    ll = [x for x in reduced_line]
    res = magnitude(ll)
    return int(res[0])


def part2(input_list):
    """ Part 2 """
    lines = []
    reduced_line = ''
    for i, line in enumerate(input_list):
        # 1. Read line
        line = [str(x) for x in line]
        # 2. Convert list to string
        line = ''.join(line)

        lines.append(line)
    max_mag = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue

            line = "[" + str(lines[i]) + "," + str(lines[j]) + "]"
            reduced_line = reduce(line)
            ll = [x for x in reduced_line]

            value = int(magnitude(ll)[0])

            if value > max_mag:
                max_mag = value

    return max_mag


def main():
    with open("./2021/Day 18/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
