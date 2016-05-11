# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11369.htm
"""

import math
def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        # sort prices in descending order
        prices = sorted(list(map(int, input().split())))[::-1]

        # number of check which can save money
        n_check = n//3
        save = sum(prices[cdx*3+2] for cdx in range(n_check))
        print (save)

if __name__ == '__main__':
    main()

