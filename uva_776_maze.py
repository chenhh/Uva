# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/776.pdf
"""

import sys
from collections import deque

directions = ((1, 0), (-1, 0), (0, 1), (0, -1),
              (1, 1), (1, -1), (-1, 1), (-1, -1))


def dfs(forest):
    global directions
    n_row = len(forest)
    n_col = len(forest[0])

    family = [[0] * n_col for _ in range(n_row)]
    species = 1
    stack = deque([(0, 0)])
    curr_rdx = 0
    family[0][0] = species

    while stack:
        x, y = stack.pop()
        # print(x, y, species)
        tree = forest[x][y]
        for dx, dy in directions:
            x1 = x + dx
            y1 = y + dy
            if (0 <= x1 < n_row and 0 <= y1 < n_col and not family[x1][y1] and
                        forest[x1][y1] == tree):
                family[x1][y1] = species
                stack.append((x1, y1))
        if not stack:
            for rdx in range(curr_rdx, n_row):
                if stack:
                    break
                for cdx in range(n_col):
                    if not family[rdx][cdx]:
                        stack.append((rdx, cdx))
                        species += 1
                        family[rdx][cdx] = species
                        curr_rdx = rdx
                        break

    # output
    col_width = [max(len(str(family[rdx][cdx])) for rdx in range(n_row))
                 for cdx in range(n_col)]
    for row in family:
        print(" ".join("{1:>{0}}".format(col_width[cdx], v)
                       for cdx, v in enumerate(row)))
    print("%")


def main():
    recs = iter(sys.stdin.readlines())
    forest = []
    forest_append = forest.append
    forest_clear = forest.clear
    while True:
        try:
            trees = next(recs).split()
            if trees[0] != '%':
                forest_append(trees)
            else:
                dfs(forest)
                forest_clear()

        except (StopIteration):
            if forest:
                dfs(forest)
            break


if __name__ == '__main__':
    main()
