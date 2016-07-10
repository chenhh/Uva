# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/111/11150.pdf
"""

import sys


def main():
    recs = sys.stdin.readlines()

    for rec in recs:
        n_bottle = int(rec)
        n_full = n_bottle
        while n_bottle >= 3:
            exchange, rem = divmod(n_bottle, 3)
            n_full += exchange
            n_bottle = exchange + rem
        if n_bottle >= 2:
            n_full += 1
        print(n_full)


if __name__ == '__main__':
    main()
