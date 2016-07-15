# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/100/10077.pdf
Stern-Brocot tree
"""

import sys


def SB_tree(m, n):
    """ binary search of fractional number """
    tgt = [m, n]
    curr = [1, 1]
    left = [0, 1]
    right = [1, 0]
    path = []
    path_append = path.append
    while curr != tgt:
        # y1/x1 < y2/x2 <=> y1 * x2 < y2 * x1
        if curr[1] * tgt[0] < tgt[1] * curr[0]:
            # left
            path_append('L')
            right[0] = curr[0]
            right[1] = curr[1]
            curr[0] += left[0]
            curr[1] += left[1]

        else:
            # right
            path_append('R')
            left[0] = curr[0]
            left[1] = curr[1]
            curr[0] += right[0]
            curr[1] += right[1]

    return "".join(path)


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        m, n = list(map(int, next(recs).split()))
        if m == 1 and n == 1:
            break
        print(SB_tree(m, n))


if __name__ == '__main__':
    main()
