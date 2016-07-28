# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

11800 Determine the Shape


https://uva.onlinejudge.org/external/118/11800.pdf

given four points, and no three of them are collinear, to
determining the shape of the four points.
"""

import sys


def gcd(x, y):
    x = abs(x)
    y = abs(y)
    if not x:
        # gcd(0, 7) = 7
        return y
    if not y:
        # gcd(7, 0) =  7
        return x

    while x % y:
        x, y = y, x % y
    return y


def shape(points):
    """
    points: list((int, int)), size: 4
    """
    # sorted by x first, then by y.
    # p1 is in the lower-left, and p4 is in upper-right
    points.sort(key=lambda x: (x[0], x[1]))

    print(points)
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = points
    vectors = []
    for idx in range(4):
        for jdx in range(idx + 1, 4):
            vx = points[jdx][0] - points[idx][0]
            vy = points[jdx][1] - points[idx][1]
            com = gcd(vx, vy)
            if com:
                vx = vx // com
                vy = vy // com
            vectors.append((vx, vy))

    (v12_x, v12_y), (v13_x, v13_y), (v14_x, v14_y), (v23_x, v_23_y), \
    (v24_x, v24_y), (v34_x, v_34_y) = vectors
    print(vectors)


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        points = [list(map(int, next(recs).split())) for _ in range(4)]
        print("Case {}: {}".format(tdx + 1, shape(points)))


if __name__ == '__main__':
    main()
