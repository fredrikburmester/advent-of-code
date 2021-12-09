"""
This was fun to write. First trick was to zero-padd the matrix to be able to ignore edge cases.

Part1: Just checking adjecent numbers and seeing if they are all less than the current number.

Part2: I wrote a check_adjecent function that checks all adjecent numbers recursivly and returns the length of the numbers
smaller than the current number. To keep track of the checked numbers I used a dictionary.

I then sorted the list of lengths and took the first three for the result.
"""
from collections import defaultdict
import time


def part1(input_list):
    """ Part 1"""
    matrix = []
    mp = []

    zeros = [11] * (len(input_list[0]) + 2)
    matrix.append(zeros)

    for line in input_list:
        line = [int(x) for x in line]
        line.append(11)
        line.insert(0, 11)
        matrix.append(line)

    matrix.append(zeros)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(zeros) - 1):
            n = matrix[row][col]

            if n < matrix[row][col+1] and n < matrix[row+1][col] and n < matrix[row-1][col] and n < matrix[row][col-1]:
                mp.append(n)

    mp = [n + 1 for n in mp]
    mp = sum(mp)
    print(mp)

    return mp


def check_adjecent(matrix, row, col, mapp):
    """
    This function checks all adjecent numbers recursivly and returns the amount
    of the numbers smaller than the current number.

    Args:
        matrix: The matrix to check
        row: The row to check
        col: The column to check
        mapp: A dictionary to keep track of the checked numbers

    Returns:
        The amount of numbers smaller than the current number
    """

    n = matrix[row][col]

    n2 = matrix[row][col + 1]
    n3 = matrix[row + 1][col]

    n4 = matrix[row - 1][col]
    n5 = matrix[row][col - 1]

    lp = []
    other = 0

    mapp[(row, col)] = 1

    if n < n2 and n2 != 11 and n2 != 9:
        if mapp[(row, col + 1)] == 0:
            lp.append(n2)
            other += check_adjecent(matrix, row, col + 1, mapp)
    if n < n3 and n3 != 11 and n3 != 9:
        if mapp[(row + 1, col)] == 0:
            lp.append(n3)
            other += check_adjecent(matrix, row + 1, col, mapp)
    if n < n4 and n4 != 11 and n4 != 9:
        if mapp[(row - 1, col)] == 0:
            lp.append(n4)
            other += check_adjecent(matrix, row - 1, col, mapp)
    if n < n5 and n5 != 11 and n5 != 9:
        if mapp[(row, col - 1)] == 0:
            lp.append(n5)
            other += check_adjecent(matrix, row, col - 1, mapp)

    return len(lp) + other


def part2(input_list):
    matrix = []
    mp = []

    zeros = [11] * (len(input_list[0]) + 2)
    matrix.append(zeros)

    for line in input_list:
        line = [int(x) for x in line]
        line.append(11)
        line.insert(0, 11)
        matrix.append(line)

    matrix.append(zeros)

    r_end = len(matrix) - 1
    c_end = len(zeros) - 1
    mapp = defaultdict(bool)

    lengths = []

    for row in range(1, r_end):
        for col in range(1, c_end):
            n = matrix[row][col]

            c1 = 1
            c2 = 1
            n2 = matrix[row-1][col-1]

            mapp.clear()
            length = check_adjecent(matrix, row, col, mapp)
            lengths.append(int(length) + 1)

    lengths.sort(reverse=True)
    print(lengths[0:3])

    return lengths[0] * lengths[1] * lengths[2]


def main():
    with open("./2021/Day 9/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
