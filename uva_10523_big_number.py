# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/105/10523.pdf
"""

import sys


def main():
    recs = sys.stdin.readlines()
    for rec in recs:
        n, a = list(map(int, rec.split()))
        print(sum(idx * a ** idx for idx in range(1, n + 1)))


if __name__ == '__main__':
    main()
