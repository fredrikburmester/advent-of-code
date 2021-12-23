"""
Started making this class based system but it's not worth it,
I just solved it by hand in like 5 minutes for part 1 and thirty minutes for part 2.

NON COMPLETE CODE: won't run... 
"""
from collections import defaultdict, deque
from copy import deepcopy
import time


def neighbours_4(board, x, y):
    def in_range(x, y):
        return min(board)[0] <= x < max(board)[0] and min(board)[1] <= y < max(board)[1]
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


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


def printBoard(board, amphipods_list):
    """ Prints the board, print a dict, print dict """
    _max = max(board)
    _min = min(board)
    for y in range(_min[1], _max[1] + 1):
        for x in range(_min[1], _max[0] + 1):
            for a in amphipods_list:
                if a.position == (x, y):
                    print(a.letter, end="")
                    break
            else:
                print(board[(x, y)], end="")
        print()


class Amphipods():
    def __init__(self, x, y, letter, id):
        self.position = (x, y)
        self.last_position = (x, y)
        self.letter = letter
        self.id = id

        if letter == 'A':
            self.cost = 1
        elif letter == 'B':
            self.cost = 10
        elif letter == 'C':
            self.cost = 100
        elif letter == 'D':
            self.cost = 1000

    def __str__(self):
        return f"{self.letter}:{self.id}, {self.position}, {self.cost}"

    def isInOwnRoomEntrence(self):
        if self.letter == 'A' and self.position == (3, 2):
            return True
        elif self.letter == 'B' and self.position == (5, 2):
            return True
        elif self.letter == 'C' and self.position == (7, 2):
            return True
        elif self.letter == 'D' and self.position == (9, 2):
            return True
        return False

    def isInOtherRoom(self):
        if not self.isInHall and not self.isOutsideRoom and not self.isInOwnRoom():
            return True
        return False

    def isInHall(self):
        if self.position[1] == 1:
            return True
        return False

    def isOutsideRoom(self):
        if self.position[1] == 1 and self.position[0] in [3, 5, 7, 9]:
            return True
        return False

    def isOutSideOwnRoom(self):
        if self.letter == 'A' and self.position == (3, 1):
            return True
        elif self.letter == 'B' and self.position == (5, 1):
            return True
        elif self.letter == 'C' and self.position == (7, 1):
            return True
        elif self.letter == 'D' and self.position == (9, 1):
            return True
        return False

    def isHome(self):
        if self.letter == 'A' and self.position == (3, 3):
            return True
        elif self.letter == 'B' and self.position == (5, 3):
            return True
        elif self.letter == 'C' and self.position == (7, 3):
            return True
        elif self.letter == 'D' and self.position == (9, 3):
            return True
        return False


def move(_from, _to, legal_moves, amphipod):
    """ Moves an amphipod from one position to another """
    if _to not in legal_moves:
        return 0

    legal_moves.remove(_to)
    legal_moves.add(_from)
    amphipod.position = _to
    amphipod.last_position = _from
    return amphipod.cost


def getLetterInPosition(amphipod_list, x, y):
    for a in amphipod_list:
        if a.position == (x, y):
            return a.letter

# def moves(amphipod_list, legal_moves):
#     moves = []
#     for a in amphipod_list:
#         if a.isInOwnRoomEntrence():
#             if (a.position[0], a.position[1] + 1) in legal_moves:
#                 moves.append((a.position[0], a.position[1] + 1))
#             elif a.letter == getLetterInPosition(amphipod_list, a.position[0], a.position[1] + 1):
#                 moves.append((a.position[0], a.position[1] - 1))
#         elif a.isOutsideOwnRoom():
#             if (a.position[0], a.position[1] + 1) in legal_moves:
#                 moves.append((a.position[0], a.position[1] + 1))
#         elif a.

#     return []


def allPossibleMoves(amphipods_list, legal_moves, board):
    moves = []
    for a in amphipods_list:
        if a.isHome():
            continue
        for n in neighbours_4(board, *a.position):
            if n in legal_moves and n not in moves:
                moves.append((n, a.cost))
    return moves


def isInOwnRoom(amphipod, amphipod_list):
    if amphipod.letter == 'A' and amphipod.position == (3, 2):
        return True
    elif amphipod.letter == 'B' and amphipod.position == (5, 2):
        return True
    elif amphipod.letter == 'C' and amphipod.position == (7, 2):
        return True
    elif amphipod.letter == 'D' and amphipod.position == (9, 2):
        return True
    return False


def isHome(amphipod, amphipods_list):
    if amphipod.letter == 'A':
        if amphipod.position == (3, 3):
            return True
        elif amphipod.position == (3, 2):
            for a in amphipods_list:
                if a.letter == 'A' and a.position == (3, 3):
                    return True
    elif amphipod.letter == 'B':
        if amphipod.position == (5, 3):
            return True
        elif amphipod.position == (5, 2):
            for a in amphipods_list:
                if a.letter == 'B' and a.position == (4, 3):
                    return True
    elif amphipod.letter == 'C':
        if amphipod.position == (7, 3):
            return True
        elif amphipod.position == (7, 2):
            for a in amphipods_list:
                if a.letter == 'C' and a.position == (7, 3):
                    return True
    elif amphipod.letter == 'D':
        if amphipod.position == (9, 3):
            return True
        elif amphipod.position == (9, 2):
            for a in amphipods_list:
                if a.letter == 'D' and a.position == (9, 3):
                    return True
    return False


def part1(input_list):
    """ Part 1"""

    board = defaultdict(int)
    amphipods_list = set()
    legal_moves = set()
    total_cost = 0

    # Load the board
    for y, line in enumerate(input_list):
        if len(line) == 9:
            line = "##" + line + "##"
        for x, c in enumerate(line):
            if c == '#':
                board[(x, y)] = "#"
            elif c == '.':
                board[(x, y)] = "."
                legal_moves.add((x, y))
            elif c in 'ABCD':
                board[(x, y)] = "."
                A = Amphipods(x, y, c, len(amphipods_list))
                amphipods_list.add(A)

    def dfs(start):
        all_states = {start: (0, None)}
        queue = deque([start])
        while queue:
            state = queue.popleft()
            cost, prev = all_states[state]
            for next_move, next_cost in allPossibleMoves(amphipods_list, legal_moves, board):
                if next in all_states and all_states[next][0] <= cost + next_cost:
                    continue
                all_states[next] = (cost + next_cost, state)
                queue.append(next)

        return all_states

    print(dfs((0, 0)))

    return 0


def part2(input_list):
    """ Part 2 """
    return 0


def main():
    with open("./2021/Day 23/input.txt", "r", encoding='UTF-8') as file:
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
