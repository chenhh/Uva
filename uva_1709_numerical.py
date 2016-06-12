# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/17/1709.pdf
maximum drop down

correct but TLE, since the python loop is very slow
"""

import sys
from math import (sin, cos)


def main():
    records = sys.stdin.readlines()

    for rec in records:
        p, a, b, c, d, n = list(map(int, rec.split()))
        peak, mad = 0, 0
        for k in range(1, n + 1):
            price = p * (sin(a * k + b) + cos(c * k + d) + 2)
            if price > peak:
                peak = price
            diff = abs(peak - price)
            if diff > mad:
                mad = diff
        print("{:.6f}".format(mad))


if __name__ == '__main__':
    main()
