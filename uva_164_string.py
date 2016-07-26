# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

164 String Computer

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/164.pdf

abcde bcgfe
edit distance
"""

import sys
from pprint import pprint


def edit_distance(X, Y):
    """
    costs of delete, insert, change actions are all 1.
    dist(idx, jdx) = min(
        dist(idx-1, jdx),   # delete
        dist(idx, jdx-1),   # insert
        dist(idx-1, jdx-1)+ cost of X[idx] != Y[jdx] # replace
    )
    """

    len_x = len(X)
    len_y = len(Y)

    # initialize
    cost = [[0] * len_y for _ in range(len_x)]

    # 0: equal, 1: delete, 2: insert, 3: replace
    path = [[0] * len_y for _ in range(len_x)]
    for jdx in range(len_y):
        cost[0][jdx] = jdx
        if X[0] != Y[jdx]:
            path[0][jdx] = 2

    for idx in range(len_x):
        cost[idx][0] = idx
        if X[idx] != Y[0]:
            path[idx][0] = 1

    for idx in range(1, len_x):
        for jdx in range(1, len_y):
            if X[idx] == Y[jdx]:
                # equal
                cost[idx][jdx] = cost[idx - 1][jdx - 1]
                path[idx][jdx] = 0
            else:
                upper = cost[idx - 1][jdx] + 1
                left = cost[idx][jdx - 1] + 1
                diagonal = cost[idx - 1][jdx - 1] + 1

                if upper <= left and upper <= diagonal:
                    # delete x[idx]
                    cost[idx][jdx] = upper
                    path[idx][jdx] = 1
                elif left <= upper and left <= diagonal:
                    # insert y[jdx]
                    cost[idx][jdx] = left
                    path[idx][jdx] = 2
                elif diagonal <= upper and diagonal <= left:
                    # replace x[idx] to y[jdx]
                    cost[idx][jdx] = diagonal
                    path[idx][jdx] = 3

    pprint(cost)
    pprint(path)

    # traceback
    curr_x = len_x - 1
    curr_y = len_y - 1
    n_action = cost[curr_x][curr_y]
    actions = []

    for _ in reversed(range(n_action)):
        while path[curr_x][curr_y] == 0:
            curr_x -= 1
            curr_y -= 1

        value = path[curr_x][curr_y]
        actions.append((curr_x, curr_y, value))
        if value == 3:
            # replace
            curr_x -= 1
            curr_y -= 1
        elif value == 2:
            # insert
            curr_y -= 1
        elif value == 1:
            # delete
            curr_x -= 1

    output = []
    xdx = 0
    for idx, jdx, val in reversed(actions):
        if value == 3:
            # replace, doesn't change size of X
            output.append("C{}{:02d}".format(Y[jdx], xdx))
        elif value == 2:
            # insert
            output.append("I{}{:02d}".format(Y[jdx], xdx))
        elif value == 1:
            # delete
            output.append("D{}{:02d}".format(X[xdx], xdx))

    return ("{}E".format("".join(output)))


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        data = next(recs).split()
        if data[0] == '#':
            break
        src, tgt = data
        print(edit_distance(' ' + src, ' ' + tgt))


if __name__ == '__main__':
    main()
