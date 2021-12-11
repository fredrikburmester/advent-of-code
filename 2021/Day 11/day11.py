"""
This took me some time to figure out since i missed that the board should be incremented by 1 before checking flashes. 
I also missed that an octapus only could flash once, or rather I missed to implement the != 0 check. 

I'd like to have a better way of counting flashes though.
"""
import time
FLASHES = 0


def neighbours(matrix, x, y):
    def in_range(x, y):
        return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1)] if in_range(*p)]


def flash(matrix, x, y):
    global FLASHES
    FLASHES += 1
    matrix[x][y] = 0
    n = neighbours(matrix, x, y)
    for coordinate in n:
        if matrix[coordinate[0]][coordinate[1]] != 0:
            matrix = increment(matrix, *coordinate)
    return matrix


def increment(matrix, x, y):
    matrix[x][y] += 1
    if matrix[x][y] > 9:
        matrix = flash(matrix, x, y)
    return matrix


def part1(input_list):
    """ Part 1"""
    global FLASHES
    matrix = [[int(x) for x in line] for line in input_list]

    steps = 100
    for _ in range(steps):
        for x, line in enumerate(matrix):
            for y, _ in enumerate(line):
                matrix[x][y] += 1

        for x, line in enumerate(matrix):
            for y, _ in enumerate(line):
                if matrix[x][y] > 9:
                    matrix = flash(matrix, x, y)

    return FLASHES


def part2(input_list):
    """ Part 2 """
    matrix = [[int(x) for x in line] for line in input_list]

    steps = 1000
    for step in range(steps):
        for x, line in enumerate(matrix):
            for y, _ in enumerate(line):
                matrix[x][y] += 1

        for x, line in enumerate(matrix):
            for y, _ in enumerate(line):
                if matrix[x][y] > 9:
                    matrix = flash(matrix, x, y)

        # check if all values in matrix is 0
        if all(all(x == 0 for x in line) for line in matrix):
            return step + 1


def main():
    with open("./2021/Day 11/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 2 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
