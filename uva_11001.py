# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/110/11001.pdf
v0: required clay to make a disc

"""

import sys
from math import sqrt


def main():
    EPS = 1e-10
    recs = sys.stdin.readlines()
    for rec in recs:
        v_total, v0 = list(map(int, rec.split()))
        if v_total == 0 and v0 == 0:
            break
        longest, cnt = 0, 0
        for idx in range(1, v_total):
            unit = v_total / idx - v0
            if unit < 0:
                # there is not enough clay
                break
            curr = 0.3 * sqrt(unit) * idx
            if abs(longest - curr) <= EPS:
                cnt = 0
            elif curr > longest:
                longest = curr
                cnt = idx
        print(cnt)


if __name__ == '__main__':
    main()
