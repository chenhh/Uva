# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/116.pdf
http://luckycat.kshs.kh.edu.tw/homework/q116.htm

move from the left to right, and to get the path with minimal weights.
The start can be any row (not necessary from the first row).

"""

import sys
from pprint import pprint

directions = ((0, 1), (1, 1), (-1, 1))


def solve(weights, n_row, n_col):
    """
    the value in the maze may be negative integer.
    """
    global directions
    cost = [weights[idx][:] for idx in range(n_row)]

    # backtrack
    path = [-1] * n_col
    for idx in range(n_row):
        for jdx in range(1, n_col):
            cost[idx][jdx] = min(
                cost[idx][jdx - 1],  # from left
                cost[(idx - 1) % n_row][jdx - 1],  # from upper left
                cost[(idx + 1) % n_row][jdx - 1],  # from lower left
            ) + weights[idx][jdx]

    pprint(cost)


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        try:
            n_row, n_col = list(map(int, next(recs).split()))
            weights = [[0] * n_col for _ in range(n_row)]
            n_val = n_row * n_col
            idx = 0
            while idx < n_val:
                data = list(map(int, next(recs).split()))
                for val in data:
                    rdx, cdx = divmod(idx, n_col)
                    weights[rdx][cdx] = val
                    idx += 1
            # process
            print(solve(weights, n_row, n_col))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
