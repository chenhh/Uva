# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/118/11877.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    cache = {}
    while True:
        n_empty = int(next(recs))
        if not n_empty:
            break

        if n_empty in cache.keys():
            print(cache[n_empty])
        else:
            key = n_empty
            n_full = 0
            while n_empty >= 3:
                exchange, rem = divmod(n_empty, 3)
                n_full += exchange
                n_empty = exchange + rem
            if n_empty >= 2:
                n_full += 1
            cache[key] = n_full
            print(n_full)


if __name__ == '__main__':
    main()
