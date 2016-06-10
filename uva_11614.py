# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/116/11614.pdf

the number of warriors to from x rows is n=(1+x)*x/2
given n (0<=n<=10**18), to find x (x**2 +x -2n = 0)
x= -1 + sqrt(1+8n)/2
"""

import math


def main():
    EPS = 1e-6
    n_case = int(input())
    for _ in range(n_case):
        n = int(input())
        # f(x) = x**2 + x - 2n
        x = (-1 + math.sqrt(1 + 8 * n)) / 2
        print(int(x))


if __name__ == '__main__':
    main()
