# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

11800 Determine the Shape


https://uva.onlinejudge.org/external/118/11800.pdf
http://blog.csdn.net/murmured/article/details/19048095

given four points, and no three of them are collinear, to
determining the shape of the four points.

assuming the four points are (a, b, c, d)
the points in the plane may be (a, b, c, d), (a, c, d, b), (a, b, c, d)

"""

import sys


def cross_prod(v1, v2):
    """
    v1: tuple(int), size: 2
    v2: tuple(int), size: 2

    cross_prod(v1, v2) = |v1| * |v2| * sin(theta)
    if cross_prod(v1, v2) == 0, then v1 is parallel to v2
    (theta = 0 or pi).

    """
    return v1[0] * v2[1] - v1[1] * v2[0]


def dot_prod(v1, v2):
    """
    v1: tuple(int), size: 2
    v2: tuple(int), size: 2

    dot_prod(v1, v2) = |v1|* |v2| * cos(theta)
    if dot_prod(v1, v2) == 0 then v1 is orthogonal to v2
    (theta = pi/2 or 3/2 pi)
    """
    return v1[0] * v2[0] + v1[1] * v2[1]


def solution(ans):
    if ans == 0:
        # the general case
        return "Ordinary Quadrilateral"

    if ans == 1:
        return "Trapezium"

    if ans == 2:
        return "Parallelogram"

    if ans == 3:
        return "Rhombus"

    if ans == 4:
        return "Rectangle"

    if ans == 5:
        return "Square"


def shape(points):
    """
    points: list((int, int)), size: 4
    (a, b, c, d)
    """
    vab = (points[1][0] - points[0][0], points[1][1] - points[0][1])
    vbc = (points[2][0] - points[1][0], points[2][1] - points[1][1])
    vcd = (points[3][0] - points[2][0], points[3][1] - points[2][1])
    vda = (points[0][0] - points[3][0], points[0][1] - points[3][1])

    vac = (points[2][0] - points[0][0], points[2][1] - points[0][1])
    vdb = (points[1][0] - points[3][0], points[1][1] - points[3][1])

    cross_abcd = cross_prod(vab, vcd)
    cross_dabc = cross_prod(vda, vbc)

    # "Ordinary Quadrilateral
    ans = 0
    if cross_abcd == 0 or cross_dabc == 0:
        # ab is parallel to cd or da is parallel to bc
        # the shape can be a Trapezium
        ans = 1

    if cross_abcd == 0 and cross_dabc == 0:
        ans = 2

        if dot_prod(vac, vdb) == 0:
            ans = 3

        if dot_prod(vab, vbc) == 0:
            ans = 4

        if dot_prod(vac, vdb) == 0 and dot_prod(vab, vbc) == 0:
            ans = 5
    return ans


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        points = [list(map(int, next(recs).split())) for _ in range(4)]
        a, b, c, d = points
        ans = shape(points)
        ans = max(ans, shape([a, c, b, d]))
        ans = max(ans, shape([a, b, d, c]))
        print("Case {}: {}".format(tdx + 1, solution(ans)))


if __name__ == '__main__':
    main()
