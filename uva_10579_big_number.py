# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/105/10579.pdf
"""

import sys


def main():
    fibs = [0, 1, 1]
    while len(str(fibs[-1])) < 1000:
        fibs.append(fibs[-1] + fibs[-2])

    recs = sys.stdin.readlines()
    for rec in recs:
        n = int(rec)
        print(fibs[n])


if __name__ == '__main__':
    main()
