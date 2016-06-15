# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/108.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    while 1:
        try:
            n_num = int(next(recs))
            n_row = n_col = (n_num + 1)
            mtx = [[0] * n_col for _ in range(n_row)]
            cnt = 0
            while cnt < n_num * n_num:
                vals = list(map(int, next(recs).split()))
                for cdx, val in enumerate(vals):
                    idx, jdx = divmod(cnt + cdx, n_num)
                    mtx[idx + 1][jdx + 1] = val
                cnt += len(vals)
            # print (mtx)
            # cumulative sum from origin (upper left) to current location
            cum_sum = [[0] * n_col for _ in range(n_row)]
            for idx in range(1, n_row):
                for jdx in range(1, n_col):
                    cum_sum[idx][jdx] = cum_sum[idx - 1][jdx] + mtx[idx][jdx]

            max_sum = -2 << 31
            for idx in range(1, n_row):
                for jdx in range(idx, n_col):
                    curr = 0
                    for kdx in range(1, n_col):
                        curr += cum_sum[jdx][kdx] - cum_sum[idx - 1][kdx]
                        max_sum = max(curr, max_sum)
                        curr = max(0, curr)
            print(max_sum)
        except (StopIteration):
            break


if __name__ == '__main__':
    main()
