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

INT_MAX = 2 << 31

def solve(weights, n_row, n_col):
    """
    the value in the maze may be negative integer.
    """
    cost = [weights[idx][:] for idx in range(n_row)]
    path = [[INT_MAX] * n_col for idx in range(n_row)]

    # traceback
    for jdx in reversed(range(n_col - 1)):
        for idx in range(n_row):
            w = weights[idx][jdx]
            left = cost[idx][jdx + 1] + w
            upper = cost[(idx - 1) % n_row][jdx + 1] + w
            lower = cost[(idx + 1) % n_row][jdx + 1] + w

            if left <= upper and left <= lower:
                cost[idx][jdx] = left
                path[idx][jdx] = min(path[idx][jdx], idx)

            if upper <= left and upper <= lower:
                cost[idx][jdx] = upper
                path[idx][jdx] = min(path[idx][jdx], (idx - 1) % n_row)

            if lower <= left and lower <= upper:
                cost[idx][jdx] = lower
                path[idx][jdx] = min(path[idx][jdx], (idx + 1) % n_row)

    # pprint (cost)
    # pprint(path)

    min_path = [0] * n_col
    min_weight = cost[0][0]
    min_path[0] = 0
    next_rdx = path[0][0]
    for idx in range(1, n_row):
        if cost[idx][0] < min_weight:
            min_weight = cost[idx][0]
            min_path[0] = idx
            next_rdx = path[idx][0]

    jdx = 1
    while jdx < n_col:
        min_path[jdx] = next_rdx
        next_rdx = path[next_rdx][jdx]
        jdx += 1

    print(" ".join(str(v + 1) for v in min_path))
    print(min_weight)


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
            solve(weights, n_row, n_col)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
