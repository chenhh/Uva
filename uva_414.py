# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

414 Machined Surfaces

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/414.pdf
"""

import sys


def solve(surfaces, n_row):
    min_blank = 26
    blanks = [0] * n_row
    for rdx, row in enumerate(surfaces):
        if row.count(row[0]) != 25:
            blanks[rdx] = sum(1 for idx in range(1, 24) if row[idx] == ' ')
        min_blank = min(min_blank, blanks[rdx])

    ans = sum(blank - min_blank for blank in blanks)
    return ans


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        n_row = int(next(recs))
        if not n_row:
            break
        # the column must be 25, and 0th and 24th must be X
        surfaces = [next(recs).strip() for _ in range(n_row)]
        print(solve(surfaces, n_row))


if __name__ == '__main__':
    main()
