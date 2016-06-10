# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/118/11805.pdf
"""


def main():
    n_case = int(input())
    for tdx in range(n_case):
        # 2 <= n <= 23, 1 <= k <=n, 1 <= p <= 200
        n, k, p = list(map(int, input().split()))
        last = (k + p) % n if (k + p) % n else n
        print("Case {}: {}".format(tdx + 1, last))


if __name__ == '__main__':
    main()
