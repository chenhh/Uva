# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/6/636.pdf
"""

import sys
from math import sqrt, floor


def int_from_base(val, base):
    """ val: string """
    res = int(val[0])
    for v in val[1:]:
        res = res * base + int(v)
    return res


def main():
    UPPER = 1000000000
    recs = iter(sys.stdin.readlines())

    for rec in recs:
        val = rec.strip()
        if val == '0':
            break
        least_base = max(int(v) for v in val) + 1

        ans = 0
        for base in range(least_base, 36):
            # built-in function
            res = int(val, base)
            if res == int(floor(sqrt(res) + 0.5) ** 2):
                ans = base
                break
        if not ans:
            for base in range(37, 100):
                # our function
                res = int_from_base(val, base)
                if res == int(floor(sqrt(res) + 0.5) ** 2):
                    ans = base
                    break

        print(ans)


if __name__ == '__main__':
    main()
