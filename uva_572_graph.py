# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/5/572.pdf
‘*’, representing the absence of oil,
‘@’, representing an oil pocket.

Two different pockets are part of the same oil deposit if they are adjacent
horizontally, vertically, or diagonally.
"""

import sys


def connected_components(graph, n_node):
    """ dfs search """
    if n_node == 0:
        return 0
    stack = [0, ]
    visited = [False] * n_node

    n_sub = 1
    while not all(visited):
        # print ("Stack:", stack)
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    stack.append(child)
        if not stack:
            for idx, val in enumerate(visited):
                if not val:
                    stack.append(idx)
                    n_sub += 1
                    break
    return n_sub


def main():
    recs = iter(sys.stdin.readlines())
    # N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    while 1:
        n_row, n_col = list(map(int, next(recs).split()))
        if n_row == 0:
            break
        deposits = [next(recs).strip() for _ in range(n_row)]
        nodes = [(rdx, cdx) for cdx in range(n_col) for rdx in range(n_row)
                 if deposits[rdx][cdx] == '@']
        node_ids = {(rdx, cdx): idx for idx, (rdx, cdx) in enumerate(nodes)}
        graph = [[node_ids[(rdx + h, cdx + v)] for h, v in directions
                  if (rdx + h, cdx + v) in node_ids.keys()]
                 for rdx, cdx in nodes]
        # print (graph)
        print(connected_components(graph, len(nodes)))


if __name__ == '__main__':
    main()
