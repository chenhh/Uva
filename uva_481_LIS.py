# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/4/481.pdf
https://saicheems.wordpress.com/2013/09/01/uva-481-what-goes-up/

longest strictly increasing sub-sequence
"""
import bisect

def LIS(seqs):
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
            pos[idx] =len(tmp_lis)
        else:
            # strictly increasing,
            loc = bisect.bisect_left(tmp_lis, seqs[idx])
            tmp_lis[loc] = seqs[idx]
            pos[idx] = loc + 1

    # traceback
    lis_len = len(tmp_lis)
    lis = [0] * lis_len
    kdx = lis_len
    for jdx in range(n_data-1, -1, -1):
        if pos[jdx] == kdx:
            lis[kdx-1] = seqs[jdx]
            kdx -= 1

    return lis

def main():
    recs = []
    while True:
        try:
            rec = int(input())
            recs.append(rec)
        except (EOFError):
            lis = LIS(recs)
            print(len(lis))
            print('-')
            for val in lis:
                print(val)
            break

if __name__ == '__main__':
    main()

