# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/497.pdf
http://luckycat.kshs.kh.edu.tw/homework/q497.htm
longest increasing sub-sequence, LIS
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
    for jdx in reversed(range(n_data)):
        if pos[jdx] == kdx:
            lis[kdx-1] = seqs[jdx]
            kdx -= 1

    return lis

def main():
    N = int(input())
    _ = input()

    for ndx in range(N):
        data = []
        while 1:
            try:
                val = input().strip()
                if not len(val):
                    hits = LIS(data)
                    print ("Max hits: {}".format(len(hits)))
                    for hit in hits:
                        print (hit)
                    break
                else:
                    data.append(int(val))

            except (EOFError):
                hits = LIS(data)
                print("Max hits: {}".format(len(hits)))
                for hit in hits:
                    print(hit)
                break

        if ndx != N-1:
            print ("")

if __name__ == '__main__':
    main()