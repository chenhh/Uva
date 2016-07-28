# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

1062 Containers

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/10/1062.pdf
"""

import bisect
import sys


def quick_lis(seqs):
    """
    Robinson-Schensted-Knuth Algorithm
    to find the last occurrence of the LIS
    """
    n_data = len(seqs)
    tmp_lis = [seqs[0], ]
    pos = [1] * n_data
    for idx in range(1, n_data):
        if seqs[idx] > tmp_lis[-1]:
            tmp_lis.append(seqs[idx])
            pos[idx] = len(tmp_lis)
        else:
            # strictly increasing,
            loc = bisect.bisect_left(tmp_lis, seqs[idx])
            tmp_lis[loc] = seqs[idx]
            pos[idx] = loc + 1

    return len(tmp_lis)


def main():
    recs = sys.stdin.readlines()
    for tdx, rec in enumerate(recs):
        data = rec.strip()
        if data == 'end':
            break

        print("Case {}: {}".format(tdx + 1, quick_lis(data)))


if __name__ == '__main__':
    main()
