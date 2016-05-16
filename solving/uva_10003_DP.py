# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: working
difficulty: 2

https://uva.onlinejudge.org/external/100/10003.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10003.htm

dynamic programming
"""

def min_cut(L, N, points):
    """
    L: integer, length of stick
    N: integer, the number of cut
    points: list of integers, the cut points on the stick

    cost[x][y] = min( cost[x][c[i]] + cost[c[i]][y] + (y-x)), x < c[i] < y,
    c[i] is the cut point, x, y is the loc on the stick.

    cost[0][10] = min (cost[0][2] + cost[2][10] + 10,
                       cost[0][4] + cost[4][10] + 10,
                       cost[0][7] + cost[7][10] + 10)
    cost[0][2] = 0, cost[7][10]= 0, because of no cut in [0,2] and [7, 10].
    other items requires further steps.
    """



def main():
    while 1:
        L = int(input())
        if not L:
            break

        N = int(input())
        points = list(map(int, input().split()))
        cost = min_cut(L, N, points)
        print ("The minimum cutting is {}.".format(cost))

if __name__ == '__main__':
    main()