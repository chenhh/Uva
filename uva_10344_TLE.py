# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/103/10344.pdf

the problem requires to visit all combinations to compute the corresponding
values is equal to 23 or not..
"""

import sys

values = [0] * 5
possible = False
chosen = [False] * 5


def solve(value, pos):
    global values, possible, chosen

    if value == 23 and pos == 5:
        possible = True
        return
    else:
        for idx in range(5):
            if not chosen[idx]:
                chosen[idx] = True
                solve(value + values[idx], pos + 1)
                solve(value - values[idx], pos + 1)
                solve(value * values[idx], pos + 1)
                chosen[idx] = False


def sequential_main():
    recs = iter(sys.stdin.readlines())
    global values, possible, chosen

    while True:
        vals = list(map(int, next(recs).split()))
        if not any(vals):
            break
        values = vals
        possible = False

        for idx in range(5):
            chosen[idx] = True
            solve(vals[idx], 1)
            chosen[idx] = False
        if possible:
            print("Possible")
        else:
            print("Impossible")


if __name__ == '__main__':
    sequential_main()
