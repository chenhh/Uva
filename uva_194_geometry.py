# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/194.pdf

there are 2^6 cases of the missing inputs.

two triangles are equal if:
    SSS, SAS, ASA, AAS

"""

import sys
from math import (pi, cos, acos, sin, asin, sqrt)

EPS = 1e-4


def edge2angle(a, b, c):
    return acos((a * a + b * b - c * c) / (2 * a * b))


def get_edge(alpha, b, c):
    return sqrt(b * b + c * c - 2 * b * c * cos(alpha))


def is_triangle(vals):
    a, alpha, b, beta, c, gamma = vals

    if a <= 0 or b <= 0 or c <= 0 or alpha <= 0 or beta <= 0 or gamma <= 0:
        # all values should be positive
        return False

    if alpha + beta + gamma - pi > EPS:
        # the sum of angle should equal to pi
        return False

    if (a + b <= c or a + c <= b or b + c <= a):
        # triangle inequality
        return False

    if (a * beta - b * alpha > EPS or a * gamma - c * alpha > EPS or
                        b * gamma - c * beta > EPS):
        # law of sine
        return False

    return True


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        # a, alpha, b, beta, c, gamma
        vals = list(map(float, next(recs).split()))

        # negative values are the unknown variables
        n_unknown_edge = 0
        n_unknown_angle = 0
        for idx, val in enumerate(vals):
            if val <= 0:
                if idx % 2:
                    n_unknown_angle += 1
                else:
                    n_unknown_edge += 1

        # print(n_unknown_edge, n_unknown_angle)
        n_unknown = n_unknown_edge + n_unknown_angle

        if n_unknown >= 4:
            # all the edges or all the angles are unknown.
            print("Invalid input.")
            continue

        if n_unknown == 0:
            # all values are known/
            print(" ".join("{:.8f}".format(v) for v in vals))
            continue

        is_multiple_sol = False
        # recover
        while n_unknown > 0:

            if n_unknown_angle == 1:
                # only one unknown angle
                if vals[1] <= 0:
                    vals[1] = pi - vals[3] - vals[5]
                elif vals[3] <= 0:
                    vals[3] = pi - vals[1] - vals[5]
                elif vals[5] <= 0:
                    vals[5] = pi - vals[1] - vals[3]
                # update
                n_unknown -= 1
                n_unknown_angle = 0

            if n_unknown_edge == 0:
                # all the edges are known, to get the corresponding angle
                # it may be two angles still unknown.
                if vals[1] <= 0:
                    a, b, c = vals[0], vals[2], vals[4]
                    vals[1] = edge2angle(a, b, c)
                if vals[3] <= 0:
                    c, a, b = vals[0], vals[2], vals[4]
                    vals[3] = edge2angle(a, b, c)
                if vals[5] <= 0:
                    c, a, b = vals[0], vals[2], vals[4]
                    vals[3] = edge2angle(a, b, c)
                # update
                n_unknown -= n_unknown_angle
                n_unknown_angle = 0

            # there are 2 unknown angles and 1 or 2 unknown edges.
            for idx in range(0, 6, 2):
                # both idx edge and angle are known
                if vals[idx] <= 0 or vals[idx + 1] <= 0:
                    continue

                for jdx in range(0, 6, 2):
                    if ((jdx == idx and
                                 vals[jdx] > 0 and vals[jdx + 1] > 0) or
                            (vals[jdx] <= 0 and vals[jdx + 1] <= 0)):
                        # both the edge and angle are known or unknown
                        continue

                    if vals[jdx] <= 0:
                        # the edge is unknown, using law of sine to recover
                        vals[jdx] = (vals[idx] / sin(vals[idx + 1]) *
                                     sin(vals[jdx + 1]))
                        # update
                        n_unknown -= 1
                        n_unknown_edge -= 1
                    else:
                        # he angle is unknown,
                        # using law of sine to recover
                        if (vals[idx + 1] < pi / 2 and vals[idx] < vals[jdx] and
                                    vals[idx] > vals[jdx] * sin(vals[idx + 1])):
                            is_multiple_sol = True
                        tmp = sin(vals[idx + 1]) * vals[jdx] / vals[idx]
                        if 0 < tmp < 1:
                            vals[jdx + 1] = asin(tmp)
                            # update
                            n_unknown -= 1
                            n_unknown_angle -= 1

            if n_unknown_edge == 1:
                # only one unknown edge
                if vals[0] <= 0 and vals[1] > 0:
                    alpha, b, c = vals[1], vals[2], vals[4]
                    vals[0] = get_edge(alpha, b, c)
                    n_unknown_edge = 0
                    n_unknown -= 1

                elif vals[1] <= 0 and vals[2] > 0:
                    alpha, b, c = vals[2], vals[0], vals[4]
                    vals[1] = get_edge(alpha, b, c)
                    n_unknown_edge = 0
                    n_unknown -= 1

                elif vals[3] <= 0 and vals[4] > 0:
                    alpha, b, c = vals[4], vals[0], vals[2]
                    vals[3] = get_edge(alpha, b, c)
                    n_unknown_edge = 0
                    n_unknown -= 1
        # end of recover

        if is_triangle(vals):
            if is_multiple_sol:
                print("More than one solution.")
            else:
                print(" ".join("{:.8f}".format(v) for v in vals))
        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()
