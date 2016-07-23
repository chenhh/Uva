# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/100/10003.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10003.htm

dynamic programming
"""

import sys
from multiprocessing.pool import Pool


def min_cut(cuts):
    """
    L: integer, length of stick
    n_cut: integer, the number of cut (containing the end points 0 and L)
    points: list of integers, the cut points on the stick

    0<=i<k<j<=L are all cutting points
    cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j]+c[j]-c[i])

    cuts=[0,2,4,7,10]
    cuts[0][1] = cuts[1][2]=cuts[2][3]=cuts[3][4] = 0

    cost[0][4] = min(
                cost[0][4],
                cost[0][1] + cost[1][4]+(c[4]-c[0]),
                cost[0][2] + cost[2][4]+(c[4]-c[0]),
                cost[0][3] + cost[3][4]+(c[4]-c[0])
                )
    cost[1][4] = min(
                cost[1][4],
                cost[1][2] + cost[2][4]+(c[4]-c[1]),
                cost[1][3] + cost[3][4]+(c[4]-c[1]),
                )
    the answer is in cost[0][n_cut]
    """
    n_cut = len(cuts)
    cost = [[0] * n_cut for _ in range(n_cut)]

    for n_pt in range(2, n_cut):
        # number of cutting points in the interval
        for idx in range(n_cut - n_pt):
            # idx: the start cutting point
            # jdx: the end cutting point
            jdx = idx + n_pt
            # print(idx, jdx)
            cuts_jdx = cuts[jdx]
            cuts_idx = cuts[idx]
            cost[idx][jdx] = 2 << 31
            cost[idx][jdx] = min(
                cost[idx][kdx] + cost[kdx][jdx] + cuts_jdx - cuts_idx
                for kdx in range(idx + 1, jdx))

            # for kdx in range(idx+1, jdx):
            #     cost[idx][jdx] = min(
            #                 cost[idx][jdx],
            #                 )

    # print(cuts)
    # print(cost)
    return "The minimum cutting is {}.".format(cost[0][n_cut - 1])


def main():
    recs = iter(sys.stdin.readlines())
    cuts = []
    cuts_extend = cuts.extend
    cuts_append = cuts.append
    cuts_clear = cuts.clear

    while True:
        # length of stick
        L = int(next(recs))
        if L == 0:
            break

        # number of cut
        n_cut = int(next(recs))
        # cutting points
        cuts_clear()
        cuts_append(0)
        cuts_extend(list(map(int, next(recs).split())))
        cuts.append(L)
        print(min_cut(cuts))


def parallel_main():
    recs = iter(sys.stdin.readlines())
    cuts_list = []
    cuts_list_append = cuts_list.append
    cuts = []
    cuts_extend = cuts.extend
    cuts_append = cuts.append
    cuts_clear = cuts.clear

    while True:
        # length of stick
        L = int(next(recs))
        if L == 0:
            break

        # number of cut
        n_cut = int(next(recs))
        # cutting points
        cuts_clear()
        cuts_append(0)
        cuts_extend(list(map(int, next(recs).split())))
        cuts_append(L)
        cuts_list_append(cuts[:])

    p = Pool(4)
    results = p.map(min_cut, cuts_list)
    for res in results:
        print(res)


if __name__ == '__main__':
    main()
    # parallel_main()
