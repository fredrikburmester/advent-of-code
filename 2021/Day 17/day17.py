"""
"""
import time


def part1(input_list):
    """ Part 1"""
    line = [x.strip() for x in input_list[0].split("x=")[1].split('y=')]
    line = [x.replace(',', '') for x in line]
    x_end = [int(n) for n in line[0].split("..")]
    y_end = [int(n) for n in line[1].split("..")]

    print(f"x: {x_end[0]}...{x_end[1]}, y: {y_end[1]}...{y_end[0]}", end="\n\n")

    x = 0
    y = 0
    ys = []
    highest = 0
    for vx0 in range(1, 100):
        for vy0 in range(100, 200):
            x, y = 0, 0
            vx, vy = vx0, vy0
            ys.clear()

            for _ in range(300):
                x += vx
                y += vy
                if x > 0 and vx > 0:
                    vx = vx - 1
                elif x < 0:
                    vx = vx + 1

                vy = vy - 1

                if x > x_end[1] or y < y_end[0]:
                    break

                ys.append(y)

                if x_end[0] <= x <= x_end[1] and y_end[0] <= y <= y_end[1]:
                    high = max(ys)
                    if high > highest:
                        highest = high
                        best = (vx0, vy0)
    return highest


def part2(input_list):
    """ Part 2 """
    line = [x.strip() for x in input_list[0].split("x=")[1].split('y=')]
    line = [x.replace(',', '') for x in line]
    x_end = [int(n) for n in line[0].split("..")]
    y_end = [int(n) for n in line[1].split("..")]

    print(f"x: {x_end[0]}...{x_end[1]}, y: {y_end[1]}...{y_end[0]}", end="\n\n")

    x = 0
    y = 0
    hit = set()
    for vx0 in range(1, 300):
        for vy0 in range(-300, 300):
            x, y = 0, 0
            vx, vy = vx0, vy0

            for _ in range(2000):
                x += vx
                y += vy
                if x > 0 and vx > 0:
                    vx = vx - 1
                elif x < 0:
                    vx = vx + 1

                vy = vy - 1

                if x > x_end[1] or y < y_end[0]:
                    break

                if x_end[0] <= x <= x_end[1] and y_end[0] <= y <= y_end[1]:
                    hit.add((vx0, vy0))
                    break

    return len(hit)


def main():
    with open("./2021/Day 17/input.txt", "r", encoding='UTF-8') as file:
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
