# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 3

https://uva.onlinejudge.org/external/1/193.pdf
"""

import sys


def coloring(graph, n_node):
    """
    backtracking coloring, the black node can't be neighbor of a black node,
    but the white node can be neighbor of all nodes.
    the graph may contain isolated nodes or disconnected components.
    0 is white, 1 is black
    """
    max_n_black, black_nodes = 0, None

    # the first node can be a white or a black node.
    stack = [(0, [0] + [-1] * (n_node - 1)), (0, [1] + [-1] * (n_node - 1))]
    while stack:
        node, n_colors = stack.pop()
        if node >= n_node:
            # assert sum(1 for c in n_colors if c == -1) == 0
            n_black = sum(n_colors)
            if n_black > max_n_black:
                max_n_black = n_black
                black_nodes = [str(idx + 1) for idx, c in enumerate(n_colors)
                               if c == 1]
            continue
        # test if the current can be a black node.
        black_used = [n_colors[neighbor]
                      for neighbor in graph[node]
                      if n_colors[neighbor] == 1]
        if not black_used:
            # the node can be a black node, the n_colors should copy by value
            n_colors[node] = 1
            stack.append((node + 1, n_colors[:]))
        # backtrack, and the node must can be a white node
        n_colors[node] = 0
        stack.append((node + 1, n_colors[:]))

    return (max_n_black, black_nodes)


def main():
    recs = iter(sys.stdin.readlines())
    n_graph = int(next(recs))

    for cdx in range(n_graph):
        # there is no blank line between two case
        n_node, n_edge = list(map(int, next(recs).split()))
        graph = [[] for _ in range(n_node)]
        for _ in range(n_edge):
            p1, p2 = list(map(int, next(recs).split()))
            graph[p1 - 1].append(p2 - 1)
            graph[p2 - 1].append(p1 - 1)
        n_black, blacks = coloring(graph, n_node)
        print(n_black)
        print(" ".join(blacks))


if __name__ == '__main__':
    main()
