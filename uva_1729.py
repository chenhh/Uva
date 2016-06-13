# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/17/1729.pdf

find the alphabet with the smallest frequency.
"""

import sys
from collections import defaultdict


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    count = defaultdict(int)

    for cdx in range(n_case):
        s = next(recs).strip()
        count.clear()
        for c in s:
            count[c] += 1

        ans = 1000000
        for adx in range(26):
            alphabet = chr(ord('a') + adx)
            if count[alphabet] < ans:
                ans = count[alphabet]
        print("Case {}: {}".format(cdx + 1, ans))


if __name__ == '__main__':
    main()
