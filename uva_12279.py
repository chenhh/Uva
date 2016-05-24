# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/122/12279.pdf

"""


def main():
    case = 0
    while 1:
        n = int(input())
        if not n:
            break
        case += 1
        values = list(map(int, input().split()))
        n_zero = sum(1 for v in values if v == 0)
        print("Case {}: {}".format(case, n - 2 * n_zero))


if __name__ == '__main__':
    main()
