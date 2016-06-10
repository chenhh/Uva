# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

the river width: d
the flow speed: v m/s
the boat speed u m/s

the combination speed of the direction is x=sqrt(v^2 + u^2)

"""

import math


def main():
    EPS = 1e-6
    n_case = int(input())

    for tdx in range(n_case):
        d, v, u = list(map(float, input().split()))
        print("Case {}: ".format(tdx + 1), end="")
        if u - v < EPS or u < EPS or v < EPS:
            print("can't determine")
        else:
            x = math.sqrt(u * u - v * v)
            # fastest path - shortest path
            print("{:.3f}".format(d / x - d / u))


if __name__ == '__main__':
    main()
