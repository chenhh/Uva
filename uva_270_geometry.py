# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/270.pdf
the points has the same directional vector are in the same line.
"""

import sys
from collections import defaultdict


def gcd(x, y):
    x, y = abs(x), abs(y)
    while x % y:
        x, y = y, x % y
    return y


def main():
    recs = sys.stdin.readlines()
    vectors = defaultdict(int)
    for rec in recs:
        x, y = list(map(int, rec.split()))
        com = gcd(x, y)
        vectors[(x // com, y // com)] += 1
    print(max(vectors.values()))


if __name__ == '__main__':
    # main()
    print(gcd(-4, -2))
