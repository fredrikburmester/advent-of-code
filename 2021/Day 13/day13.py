"""
Quite simple actually, but it took me some time to code. I also switched the x & y
coordinates in my head so that messed some things up.
"""


import time


def help_func():
    pass


def part(input_list):
    """ Part 1"""
    input_coords = []
    for line in input_list:
        if "=" in line:
            continue
        if len(line) > 0:
            line = [int(x) for x in line.split(",")]
            input_coords.append(line)

    max_x = max(input_coords, key=lambda x: x[0])[0]
    max_y = max(input_coords, key=lambda x: x[1])[1]

    matrix = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    for pair in input_coords:
        matrix[pair[1]][pair[0]] = 1

    for line in input_list:
        if "=" in line:
            if "x" in line:
                matrix = foldx(matrix, int(line.split("=")[-1]))
            elif "y" in line:
                matrix = foldy(matrix, int(line.split("=")[-1]))

            count = 0
            for line in matrix:
                for n in line:
                    if n > 0:
                        count += 1
            print(f"Number of dots on paper: {count}")

    print()
    for line in matrix:
        for n in line:
            print("X", end="") if n > 0 else print(" ", end="")
        print()
    print()


def foldy(matrix, fold_y):
    matrix1 = matrix[0:fold_y]
    matrix2 = matrix[fold_y+1:][::-1]
    assert len(matrix1) == len(matrix2)
    matrix3 = []
    for i, line in enumerate(matrix1):
        sum_lines = [sum(x) for x in zip(matrix1[i], matrix2[i])]
        matrix3.append(sum_lines)
    return matrix3


def foldx(matrix, fold_x):
    matrix3 = []
    for line in matrix:
        line1 = line[0:fold_x]
        line2 = line[fold_x+1:][::-1]
        assert len(line1) == len(line2)
        sum_lines = [sum(x) for x in zip(line1, line2)]
        matrix3.append(sum_lines)
    return matrix3


def main():
    with open("./2021/Day 13/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    part(input_list)
    t1 = time.time()
    print(f"{t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
