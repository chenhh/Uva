# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/12/1260.pdf
"""

import sys


def brutal(values, n_val):
    """ O(n**2) """
    ans = sum(1 for idx in range(1, n_val)
              for jdx in range(idx)
              if values[jdx] <= values[idx])
    return ans


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        n_val = int(next(recs))
        values = list(map(int, next(recs).split()))
        print(brutal(values, n_val))


if __name__ == '__main__':
    main()
