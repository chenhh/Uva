# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/117/11723.pdf
"""


def main():
    n_case = 0
    while 1:
        n, r = list(map(int, input().split()))
        if n == 0:
            break
        n_case += 1
        # n <= r * (1+x), 0<= x <= 26
        x, res = divmod(n - r, r)
        x += 1 if res else 0
        if 0 <= x <= 26:
            print("Case {}: {}".format(n_case, x))
        else:
            print("Case {}: impossible".format(n_case))


if __name__ == '__main__':
    main()
