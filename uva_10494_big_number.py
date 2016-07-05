# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/104/10494.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        try:
            eq = next(recs)
            if '/' in eq:
                eq = eq.replace('/', '//')
            print(eval(eq))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
