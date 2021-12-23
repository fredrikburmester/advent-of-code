"""
I don't know when i got the correct answer but this worked for my input one time today at least...
It's been a super strange day and i've gotten a bunch of wrong results that i thought were right...

Maybe this will work for your input!
"""
import time


def neighbours(x: int, y: int, min_x: int, max_x: int, min_y: int, max_y: int):
    """ Assume all 9 slots in THE CORRECT ORDER (top left to bottom right) """
    def in_range(x, y):
        return min_x <= x <= max_x and min_y <= y <= max_y
    for p in [(x-1, y-1), (x, y - 1),  (x+1, y-1), (x - 1, y), (x, y), (x + 1, y), (x-1, y+1), (x, y + 1), (x+1, y+1)]:
        if in_range(*p):
            yield p
        else:
            yield None


def min_max_of_set(input_set: set) -> list:
    """ Returns the min and max x and y values of a set """
    min_x, max_x = float('inf'), 0
    min_y, max_y = float('inf'), 0
    for s in input_set:
        if s[0] < min_x:
            min_x = s[0]
        if s[0] > max_x:
            max_x = s[0]
        if s[1] < min_y:
            min_y = s[1]
        if s[1] > max_y:
            max_y = s[1]

    return [min_x, max_x, min_y, max_y]


def printDict(mapp) -> None:
    rows = []
    cols = []
    for coord in mapp:
        cols.append(coord[0])
        rows.append(coord[1])

    min_row = min(rows)
    max_row = max(rows)
    min_col = min(cols)
    max_col = max(cols)

    print(f"min_col: {min_col}, min_row: {min_row}, max_col: {max_col}, max_row: {max_row}")

    matrix = [["." for i in range(min_col, max_col+1)] for j in range(min_row, max_row+1)]

    for k, v in mapp.items():
        x = k[0]
        y = k[1]
        matrix[y][x] = v

    print("Printing dictionary:")
    for line in matrix:
        for c in line:
            print(c, end="")
        print()


def part1(input_list, steps):
    lights = set()
    algorithm = input_list[0]
    for y, row in enumerate(input_list[2:]):
        for x, cell in enumerate(row):
            if cell == '#':
                lights.add((x, y))

    # Get min and max set values
    min_x, max_x, min_y, max_y = min_max_of_set(lights)

    inf = '.'
    for _ in range(steps):
        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1

        new_lights = set(lights)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                index: str = '0'
                for n in neighbours(x, y, min_x, max_x, min_y, max_y):
                    if n in lights:
                        index += '1'
                    else:
                        index += '0'
                index = int(index, 2)
                if algorithm[index] == '#':
                    new_lights.add((x, y))
                else:
                    new_lights.discard((x, y))
        inf = algorithm[-1 if inf == '#' else 0]
        lights = new_lights

    return len(lights)


def part2(input_list, steps):
    return part1(input_list, steps)


def main():
    with open("./2021/Day 20/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list, 2)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list, 50)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
