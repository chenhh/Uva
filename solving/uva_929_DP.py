# -*- coding: utf-8 -*-
"""
# -*- coding: utf-8 -*-
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/9/929.pdf

1
4
5
0 9 9 9 9
0 9 0 0 0
0 0 0 9 0
9 9 9 9 0
the correct answer is 0, not 9.
"""

import sys


def min_travrsal(maze, n_row, n_col):
    cost = [[0] * n_col for _ in range(n_row)]

    cost[0][0] = maze[0][0]
    for jdx in range(1, n_col):
        cost[0][jdx] = maze[0][jdx] + cost[0][jdx - 1]

    for idx in range(1, n_row):
        cost[idx][0] = maze[idx][0] + cost[idx - 1][0]

    for idx in range(1, n_row):
        for jdx in range(1, n_col):
            cost[idx][jdx] = min(cost[idx - 1][jdx] + maze[idx][jdx],
                                 cost[idx][jdx - 1] + maze[idx][jdx])
    return cost[n_row - 1][n_col - 1]


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    while n_case:
        n_row = int(next(recs))
        n_col = int(next(recs))

        maze = [list(map(int, next(recs).split())) for _ in range(n_row)]
        print(min_travrsal(maze, n_row, n_col))

        # update
        n_case -= 1


if __name__ == '__main__':
    main()
