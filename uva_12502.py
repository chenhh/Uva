# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12502.pdf

each family should spend 3 hours for cleaning its part.
Family A spend 5 hours, then there are 2 hours for family C.
Family B spend 3 hours, then there are 1 hours for family C.
90 * 2/3 = 60

assume the total cleaning time costs 3*h=(x+y) hours
family A: family B = x-(x+y)/3 : y-(x+y)/3 = (2x-y)/3 : (-x+2y)/3
family A get z * (2x-y)/((2x-y) + (-x+2y)) = z * (2x-y)/(x+y)
"""


def main():
    n_case = int(input())
    for _ in range(n_case):
        x, y, z = list(map(int, input().split()))
        print(int(z * (2 * x - y) / (x + y)))


if __name__ == '__main__':
    main()
