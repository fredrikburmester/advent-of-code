import sys
from collections import deque


# A class to represent a graph object
class Graph:
    # Graph Constructor
    def __init__(self, edges, n):

        # resize the list to `n` elements
        self.adjList = [[] for _ in range(n)]

        # add edges to the directed graph
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))


# Perform BFS on graph `g` starting from vertex `v`
def findLeastCost(g, src, dest, m):

    # create a queue for doing BFS
    q = deque()

    # enqueue source vertex
    q.append((src, 0, 0))

    # stores least-cost from source to destination
    minCost = sys.maxsize

    # loop till queue is empty
    while q:

        # dequeue front node
        v, depth, cost = q.popleft()

        # if the destination is reached and BFS depth is equal to `m`,
        # update the minimum cost calculated so far
        if v == dest and depth == m:
            minCost = min(minCost, cost)

        # don't consider nodes having a BFS depth more than `m`.
        # This check will result in optimized code and handle cycles
        # in the graph (otherwise, the loop will never break)
        if depth > m:
            break

        # do for every adjacent edge of `v`
        for (des, weight) in g.adjList[v]:
            # push every vertex (discovered or undiscovered) into
            # the queue with depth as +1 of parent and cost equal
            # to the cost of parent plus the current edge weight
            q.append((des, depth + 1, cost + weight))

    # return least-cost
    return minCost


if __name__ == '__main__':

    # List of graph edges as per the above diagram
    edges = [
        (0, 6, -1), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, 8), (3, 4, 10),
        (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6)
    ]

    # total number of nodes in the graph (labelled from 0 to 7)
    n = 8

    # build a graph from the given edges
    g = Graph(edges, n)

    (src, dest) = (0, 3)
    m = 4

    # Perform modified BFS traversal from source vertex `src`
    print(findLeastCost(g, src, dest, m))
