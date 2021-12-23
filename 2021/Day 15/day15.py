"""
I got help for the second part, but the first part is a dijkstras algorithm.

Part 1:
    The thing is that the matrix needs to be converted to a graph of nodes first.
    I've never done this before so it took me a long time.

    I then redid part 1 with the heap solution after I understood it.

Part 2:
    This is a heap approch of BFS with some fancy math.

Result:
    Part 1:
        Dijkstra's algorithm: 54.02876 seconds
        Heap solution: 0.0348992 seconds
    Part 2:
        Dijkstra's algorithm: N/A
        Heap solution: 0.68231 seconds

Note:
    The matrix in Part 2 has 25 times more elements and still the heap solution for
    Part 2 is faster than dijkstra's for Part 1...
"""
from collections import defaultdict, deque
import time
from heapq import heappop, heappush
from queue import PriorityQueue
import math


# Assume all directions
def neighbours_4_dict_2(matrix, x, y):
    def in_range(x, y):
        return 0 <= x <= max(matrix.items(), key=lambda a: a[0])[0][0] and 0 <= y <= max(matrix.items(), key=lambda a: a[0])[0][1]
    return [p for p in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if in_range(*p)]


def neighbours_4(matrix, x, y):
    def in_range(x, y):
        return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


def neighbours_4_range(x, y, end):
    def in_range(x, y):
        return 0 <= y < end[1] and 0 <= x < end[0]
    return [p for p in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if in_range(*p)]


def dijkstra(graph, start, end):
    seen, queue = set(), [(start, 0)]

    while queue:
        node, cost = queue.pop(0)
        if node == end:
            return cost

        if node in seen:
            continue
        seen.add(node)

        for neighbor_node, neighbor_cost in graph[node]:
            queue.append((neighbor_node, cost + neighbor_cost))

        queue = sorted(queue, key=lambda item: item[1])

    return 0


def part1(input_list):
    # Import list as dict
    matrix = defaultdict(int)
    for i, line in enumerate(input_list):
        for j, n in enumerate(line):
            matrix[(j, i)] = int(n)

    # Convert to a graph of nodes
    graph = {}
    for c, val in matrix.items():
        x, y = c
        links = []
        for n in neighbours_4_dict_2(matrix, x, y):
            val = matrix[n]
            links.append((n, val))
        graph[c] = links

    # Use dijkstra to find the least cost path
    return dijkstra(graph, (0, 0), (max(matrix)[0], max(matrix)[1]))


def part1_1(input_list):
    heap, visited = [(0, 0, 0)],  {(0, 0)}
    matrix = [list(map(int, line)) for line in input_list]

    ly = len(matrix)
    lx = len(matrix[0])

    while heap:
        distance, x, y = heappop(heap)
        if x == lx - 1 and y == ly - 1:
            return distance

        for x_, y_ in neighbours_4(matrix, x, y):
            a, am = divmod(x_, lx)
            b, bm = divmod(y_, ly)
            n = ((matrix[am][bm] + a + b) - 1) % 9 + 1

            if (x_, y_) not in visited:
                visited.add((x_, y_))
                heappush(heap, (distance + n, x_, y_))


def min_cost(matrix, start, end):
    visited = defaultdict(lambda: math.inf, {(0, 0): 0})
    queue = PriorityQueue()
    queue.put((0, (0, 0)))

    while queue:
        cost, current = queue.get()

        if current == end:
            return cost

        x, y = current
        for x_next, y_next in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
            if 0 <= x_next < len(matrix[0]) and 0 <= y_next < len(matrix):
                weight = matrix[y_next][x_next]
                if weight is not None:
                    cost_new = cost + weight
                    if cost_new < visited[(x_next, y_next)]:
                        visited[(x_next, y_next)] = cost_new
                        queue.put((cost_new, (x_next, y_next)))


def part1_2(input_list):
    matrix = [list(map(int, line)) for line in input_list]

    lx = len(matrix[0])
    ly = len(matrix)

    minn = min_cost(matrix, (0, 0), (lx-1, ly-1))
    print(minn)
    return minn


def part2(input_list):
    """ Part 2 """
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    matrix = [list(map(int, line)) for line in input_list]

    ly = len(matrix)
    lx = len(matrix[0])

    while heap:
        distance, x, y = heappop(heap)
        if x == 5 * lx - 1 and y == 5 * ly - 1:
            return distance

        for x_, y_ in neighbours_4_range(x, y, (lx * 5, ly * 5)):
            kvot_x, remainder_x = divmod(x_, lx)
            kvot_y, remainder_y = divmod(y_, ly)
            n = ((matrix[remainder_y][remainder_x] + kvot_x + kvot_y) - 1) % 9 + 1

            if (x_, y_) not in seen:
                seen.add((x_, y_))
                heappush(heap, (distance + n, x_, y_))


def main():
    with open("./2021/Day 15/input.txt", "r", encoding='UTF-8') as file:
        input_list = [str(line.strip()) for line in file]

    t0 = time.time()
    result = part1(input_list)
    t1 = time.time()
    print(f"{result} is the result of part 1 in {t1-t0} seconds\n")

    t0 = time.time()
    result2 = part2(input_list)
    t1 = time.time()
    print(f"{result2} is the result of part 2 in {t1-t0} seconds\n")
    print(part1_2(input_list))


# Run main function
if __name__ == "__main__":
    main()
