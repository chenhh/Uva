# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12527.pdf
"""

import sys


def main():
    counts = [1 if len(set(list(str(idx)))) == len(str(idx)) else 0
              for idx in range(5001)]
    records = sys.stdin.readlines()
    for line in records:
        n, m = list(map(int, line.split()))
        print(sum(counts[n:m + 1]))


if __name__ == '__main__':
    main()
