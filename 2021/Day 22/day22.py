"""
Brute force for part 1 and cube intersection for part 2. Quite simple in theory but was a bit
tricky to program. 
"""
from collections import Counter
from copy import deepcopy
import time


def add_cubes(x, y, z):
    assert x[0] <= x[1]
    assert y[0] <= y[1]
    assert z[0] <= z[1]

    xl = abs(x[1] - x[0]) + 1
    yl = abs(y[1] - y[0]) + 1
    zl = abs(z[1] - z[0]) + 1

    return xl*yl*zl


def part1(input_list):
    """ Part 1"""

    mapp = set()

    for _, line in enumerate(input_list):
        on = True
        if line.split(' ')[0] != 'on':
            on = False

        x, y, z = line.split(" ")[1].split(",")

        x = [int(x) for x in x[2:].split("..")]
        y = [int(y) for y in y[2:].split("..")]
        z = [int(z) for z in z[2:].split("..")]

        for i in range(x[0], x[1] + 1):
            if i < -50 or i > 50:
                continue
            for j in range(y[0], y[1] + 1):
                if j < -50 or j > 50:
                    continue
                for k in range(z[0], z[1] + 1):
                    if k < -50 or k > 50:
                        continue
                    if on:
                        mapp.add((i, j, k))
                    else:
                        mapp.discard((i, j, k))

    return len(mapp)


def part2_2(input_list):
    cuboids = Counter()
    for line in input_list:
        value = 1 if line.split()[0] == "on" else -1
        x, y, z = line.split(" ")[1].split(",")
        x0, x1 = [int(x) for x in x[2:].split("..")]
        y0, y1 = [int(y) for y in y[2:].split("..")]
        z0, z1 = [int(z) for z in z[2:].split("..")]

        # Go through all prevoius cuboids get the intersecting range and decrease/increase
        # that value.
        new_cuboids = Counter()
        for (x0_prev, x1_prev, y0_prev, y1_prev, z0_prev, z1_prev), old_value in cuboids.items():
            x0_new = max(x0, x0_prev)
            x1_new = min(x1, x1_prev)
            y0_new = max(y0, y0_prev)
            y1_new = min(y1, y1_prev)
            z0_new = max(z0, z0_prev)
            z1_new = min(z1, z1_prev)
            if x0_new <= x1_new and y0_new <= y1_new and z0_new <= z1_new:
                new_cuboids[(x0_new, x1_new, y0_new, y1_new, z0_new, z1_new)] -= old_value
        # If the value is positive, just add the range to the Counter
        if value > 0:
            new_cuboids[(x0, x1, y0, y1, z0, z1)] += value
        cuboids.update(new_cuboids)

    total = 0
    # +1 sicne x1 - x0 will result in the length of the cuboid - 1.
    for (x0, x1, y0, y1, z0, z1), value in cuboids.items():
        total += (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * value

    return total


def main():
    with open("./2021/Day 22/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2_2(input_list)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
