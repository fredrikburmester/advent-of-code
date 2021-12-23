"""
"""
from collections import defaultdict
import time
import functools


def part1(p1p, p2p):
    """ Part 1"""
    p1s, p2s = 0, 0

    running = True

    def calculate_position(pos):
        return 10 if pos % 10 == 0 else pos % 10

    def calculate_increment(throw, n):
        return (throw + n) if (throw + n) <= 100 else (throw + n) % 100

    total_throws = 0
    turn = False
    starting_pos = 1
    while running:
        # print(f"Starting throw: {starting_pos}")
        for throw in range(starting_pos, 101, 3):
            total_throws += 3
            turn = not turn

            throw = calculate_increment(throw, 0)
            throw2 = calculate_increment(throw, 1)
            throw3 = calculate_increment(throw, 2)

            if turn:
                p1p = calculate_position(p1p + throw + throw2 + throw3)
                p1s += p1p
            else:
                p2p = calculate_position(p2p + throw + throw2 + throw3)
                p2s += p2p

            starting_pos = calculate_increment(throw, 3)

            if p1s >= 1000 or p2s >= 1000:
                running = False
                print(f"Player 1: {p1s}, Player 2: {p2s}, Throws: {total_throws}")
                break

    return min(p1s, p2s) * total_throws


def calculate_pos(pos):
    return pos if pos == 10 else pos % 10


def part2(p1p_in, p2p_in):
    """ Part 2 """
    @functools.lru_cache(maxsize=None)
    def calculate_win(p1p, p1s, p2p, p2s):
        player1_win = 0
        player2_win = 0
        for throw1 in range(1, 4):
            for throw2 in range(1, 4):
                for throw3 in range(1, 4):
                    # Set new position and score
                    p1p_new = calculate_pos(p1p + throw1 + throw2 + throw3)
                    p1s_new = p1s + p1p_new

                    # Base case, if p1 winns
                    if p1s_new >= 21:
                        player1_win += 1
                    else:
                        p2w_new, p1w_new = calculate_win(p2p, p2s, p1p_new, p1s_new)
                        player1_win += p1w_new
                        player2_win += p2w_new
        return player1_win, player2_win

    print(calculate_win(p1p_in, 0, p2p_in, 0))
    return 0


def main():
    t0 = time.time()
    result = part1(10, 8)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(10, 8)
    t1 = time.time()

    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")


# Run main function
if __name__ == "__main__":
    main()
