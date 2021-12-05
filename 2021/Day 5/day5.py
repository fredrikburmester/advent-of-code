"""
Todays was more thinking than progamming.
"""


def draw_negative_line(x1, _, y1, y2, matrix):
    col = x1
    for row in range(y1, y2+1):
        matrix[row][col] += 1
        col += 1
    return matrix


def draw_positive_line(x1, _, y1, y2, matrix):
    col = x1
    for row in range(y1, y2-1, -1):
        matrix[row][col] += 1
        col += 1
    return matrix


def part1(input_list):
    # Guessing max size of the matrix
    size = 1000

    # Create the matrix filled with zeros
    matrix = [[0 for i in range(size)] for j in range(size)]

    # Read in and parse each line
    for line in input_list:
        pair1, pair2 = line.split('->')
        x1, y1 = pair1.split(',')
        x1, y1 = int(x1.strip()), int(y1.strip())
        x2, y2 = pair2.split(',')
        x2, y2 = int(x2.strip()), int(y2.strip())

        # Horrizonal and vertical line
        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for row in range(y1, y2+1):
                for col in range(x1, x2+1):
                    matrix[row][col] += 1

    # Optional: print the matrix
    if size < 100:
        for line in matrix:
            print(line)
    else:
        print("Matrix too large to print.")

    # Count numbers larger than 2 in the matrix
    res = 0
    for line in matrix:
        for number in line:
            if number > 1:
                res += 1

    return res


def part2(input_list):

    # Guessing max size of the matrix
    size = 1000

    # Create the matrix filled with zeros
    matrix = [[0 for i in range(size)] for j in range(size)]

    # Read in and parse each line
    for line in input_list:
        pair1, pair2 = line.split('->')
        x1, y1 = pair1.split(',')
        x1, y1 = int(x1.strip()), int(y1.strip())
        x2, y2 = pair2.split(',')
        x2, y2 = int(x2.strip()), int(y2.strip())

        # Horrizonal and vertical line
        if x1 == x2 or y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            for row in range(y1, y2+1):
                for col in range(x1, x2+1):
                    matrix[row][col] += 1
        else:
            # Diagnol line. Four cases with 2 draw methods.
            if x1 < x2 and y1 < y2:
                matrix = draw_negative_line(x1, x2, y1, y2, matrix)

            if x1 > x2 and y1 > y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
                matrix = draw_negative_line(x1, x2, y1, y2, matrix)

            if x1 < x2 and y1 > y2:
                matrix = draw_positive_line(x1, x2, y1, y2, matrix)

            if x1 > x2 and y1 < y2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
                matrix = draw_positive_line(x1, x2, y1, y2, matrix)

    # Optional: print the matrix
    if size < 100:
        for line in matrix:
            print(line)
    else:
        print("Matrix too large to print.")

    # Count numbers larger than 2 in the matrix
    res = 0
    for line in matrix:
        for number in line:
            if number > 1:
                res += 1

    return res


def main():
    with open("./2021/Day 5/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    result = part1(input_list)
    print(f"{result} is the result of part 1\n")

    result2 = part2(input_list)
    print(f"{result2} is the result of part 2\n")


# Run main function
if __name__ == "__main__":
    main()
