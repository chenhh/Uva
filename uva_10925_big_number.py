# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10925.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())

    case = 0
    while True:
        n_item, n_friend = list(map(int, next(recs).split()))
        if not n_item:
            break
        total_pay = sum(int(next(recs)) for _ in range(n_item))
        pay = total_pay // n_friend
        case += 1
        print("Bill #{} costs {}: each friend should pay {}".format(
            case, total_pay, pay))
        print()


if __name__ == '__main__':
    main()
