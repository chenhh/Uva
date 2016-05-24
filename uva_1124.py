# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/11/1124.pdf
"""

import sys


def main():
    records = sys.stdin.readlines()
    for line in records:
        print(line.strip())


if __name__ == '__main__':
    main()
