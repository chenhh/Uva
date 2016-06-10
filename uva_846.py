# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/8/846.pdf

The length of a step must be non-negative and can be by one bigger than,
equal to, or by one smaller than the length of the previous step

0 step, the longest distance 0
1 step, the longest distance 1
2 steps, the longest distance 2 (1, 1)
3 steps, the longest distance 4 (1, 2, 1)
4 steps, the longest distance 6 (1, 2, 2, 1)
5 steps, the longest distance 9 (1, 2, 3, 2, 1)
6 steps, the longest distance 12 (1, 2, 3, 3, 2, 1)
7 steps, the longest distance 16 (1, 2, 3, 4, 3, 2, 1)
n steps (n is even), the longest distance n/2*(n/2+1) (1,...,n/2,n/2...,1)
n steps,(n is odd), the longest distance (n-1)/2*((n-1)/2+1)
            (1,...,(n-1)/2, n, (n-1)/2,....1)
given distance d, to find the minimum n
n**2/4 + n/2 - d = 0
(n-1)**2/4 + (n-1)/2 - d = 0

"""
import math


def main():
    n_case = int(input())
    for _ in range(n_case):
        x, y = list(map(int, input().split()))
        dist = y - x
        if dist == 0:
            print(0)
        else:
            step = int(math.sqrt(dist))
            if step * step == dist:
                step = step * 2 - 1
            elif step * step + step < dist:
                step = step * 2 + 1
            else:
                step = step * 2
            print(step)


if __name__ == '__main__':
    main()
