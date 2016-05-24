# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10341.pdf
"""
import sys
from math import (exp, sin, cos, tan)


def equation(p, q, r, s, t, u, x):
    """
    0 <= x <=1, the equation is a decreasing function with the constraint.
    we can use the binary search to get solution x given the parameters.
    0<=p, r<=20 and -20<=q, s, t<=0
    """
    return (p * exp(-x) + q * sin(x) + r * cos(x) +
            s * tan(x) + t * x * x + u)


def main():
    # read all data once
    data = sys.stdin.readlines()
    EPS = 1e-10
    for line in data:
        p, q, r, s, t, u = list(map(int, line.split()))
        if equation(p, q, r, s, t, u, 1) > EPS or p + r + u < 0:
            # it's a decreasing function, if x=1 and f != 0 then no solution.
            print("No solution")
            continue

        lo, hi = 0.0, 1.0
        for idx in range(30):
            mi = (lo + hi) / 2
            f = equation(p, q, r, s, t, u, mi)
            if f > 0:
                lo = mi
            else:
                hi = mi

        print("{:.4f}".format(lo))


if __name__ == '__main__':
    main()
