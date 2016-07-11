# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/110/11078.pdf
"""

import sys


def brutal(values):
    """ O(n**2), correct, but TLE """
    max_diff = -2 << 31

    for idx, val in enumerate(values[:-1]):
        diff = max(val - v for v in values[idx + 1:])
        max_diff = max(max_diff, diff)
    return max_diff


def linear(values):
    """ O(n) """
    diff = values[0] - values[1]
    curr_max = values[0]

    for idx in range(1, len(values)):
        diff = max(diff, curr_max - values[idx])
        curr_max = max(curr_max, values[idx])

    return diff


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for _ in range(n_case):
        n_value = int(next(recs))
        values = [int(next(recs)) for _ in range(n_value)]

        print(linear(values))


if __name__ == '__main__':
    main()
