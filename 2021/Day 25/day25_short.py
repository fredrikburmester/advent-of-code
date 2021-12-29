"""
Kinda proud that I could make it this short.

Adds the fist letter of a line to the end. Then string replacement.
Handle special case for wrapping around to the beginning. 

For the down direction we transpose the matrix first. 

Runs in 0.3061 seconds on my M1 Mac with the full input.
"""
import time


def part1_string(input_list):
    def move(matrix, sym):
        for i, l in enumerate(matrix):
            ll = l[0]
            l = (l + l[0]).replace(f'{sym}.', f'.{sym}')
            matrix[i] = ''.join(l[-1] + l[1:-1]) if l[-1] != ll else ''.join(l[:-1])
        return matrix

    matrix = input_list
    step = 0
    while 1:
        step += 1
        right_next = [''.join(line) for line in zip(*move(matrix, '>'))]
        down_new = [''.join(line) for line in zip(*move(right_next, 'v'))]
        if matrix == down_new:
            return step + 3
        matrix = down_new


with open("./2021/Day 25/input.txt", "r", encoding='UTF-8') as file:
    input_list = [str(line.strip()) for line in file]

t0 = time.time()
result = part1_string(input_list)
t1 = time.time()
print(f"{result} in {round(t1-t0, 4)} seconds")
