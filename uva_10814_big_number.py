# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/108/10814.pdf
"""

import sys


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for _ in range(n_case):
        v1, v2 = list(map(int, next(recs).split('/')))
        com = gcd(v1, v2)
        print("{} / {}".format(v1 // com, v2 // com))


if __name__ == '__main__':
    main()
