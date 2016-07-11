# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/104/10487.pdf
"""

import sys
from bisect import bisect_left


def main():
    recs = iter(sys.stdin.readlines())
    case = 0

    while True:
        n_val = int(next(recs))
        if not n_val:
            break
        values = [int(next(recs)) for _ in range(n_val)]
        pair_sum = sorted(values[idx] + values[jdx]
                          for idx in range(n_val)
                          for jdx in range(idx + 1, n_val))
        n_pair = len(pair_sum)
        case += 1
        print("Case {}:".format(case))

        n_query = int(next(recs))
        for _ in range(n_query):
            query = int(next(recs))
            idx = bisect_left(pair_sum, query)
            if idx == n_pair:
                # the query is the largest lvaue among all sums.
                ans = pair_sum[idx - 1]
            elif idx == 0:
                # the query is the smallest value among all sums.
                ans = pair_sum[idx]
            elif query == pair_sum[idx]:
                # the pair sum is equal to the query
                ans = query
            else:
                # no ties
                # print (pair_sum)
                # print (idx, query)
                prev_diff = query - pair_sum[idx - 1]
                next_diff = pair_sum[idx] - query
                if prev_diff < next_diff:
                    ans = pair_sum[idx - 1]
                else:
                    ans = pair_sum[idx]

            print("Closest sum to {} is {}.".format(query, ans))


if __name__ == '__main__':
    main()
