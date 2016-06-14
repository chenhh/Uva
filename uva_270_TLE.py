# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/2/270.pdf
http://www.algorithmist.com/index.php/UVa_270
"""

import sys
from functools import cmp_to_key


def solve1(points):
    """
    O(n**3), TLE
    3 points in the same line (x1, y1), (x2, y2), (x3, y3)
    (y2-y1)/(x2-x1) = (y3-y2)/(x3-x2), then we can get
    (y2-y1) * (x3-x2) = (y3-y2)*(x2-x1)
    """
    max_line = 0
    n_points = len(points)
    for idx in range(n_points):
        x1, y1 = points[idx]
        for jdx in range(idx + 1, n_points):
            x2, y2 = points[jdx]
            line = 2
            diff_x, diff_y = (x2 - x1), (y2 - y1)
            for kdx in range(jdx + 1, n_points):
                if kdx != idx and kdx != jdx:
                    x3, y3 = points[kdx]
                    if diff_y * (x3 - x2) == (y3 - y2) * diff_x:
                        line += 1
            if line > max_line:
                max_line = line
    return max_line


def gcd(x, y):
    if y == 0:
        return x

    x, y = abs(x), abs(y)
    while x % y:
        x, y = y, x % y
    return y


def solve2(points):
    """ time complexity O(n*n*log(n)), still TLE"""
    n_point = len(points)
    vectors = []
    append = vectors.append
    ans = 1
    for idx in range(n_point):
        x1, y1 = points[idx]
        vectors.clear()
        for jdx in range(idx + 1, n_point):
            x2, y2 = points[jdx]
            diff_x, diff_y = (x1 - x2), (y1 - y2)
            com = gcd(diff_x, diff_y)
            append((diff_x // com, diff_y // com))

        vectors.sort(key=cmp_to_key(cmp_func))

        cnt = 1
        for idx in range(1, len(vectors)):
            if vectors[idx] != vectors[idx - 1]:
                cnt = 1
            else:
                cnt += 1
                ans = max(cnt, ans)
    return ans + 1


def solve3(points):
    n_point = len(points)
    ans = 1
    for idx in range(n_point - 1):
        vectors = [normalize_vector(points[idx], points[jdx])
                   for jdx in range(idx + 1, n_point)]
        vectors.sort(key=cmp_to_key(cmp_func))

        cnt = 1
        for idx in range(1, len(vectors)):
            if vectors[idx] != vectors[idx - 1]:
                cnt = 1
            else:
                cnt += 1
                ans = max(cnt, ans)

    return ans + 1


def normalize_vector(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    diff_x, diff_y = (x1 - x2), (y1 - y2)
    com = gcd(diff_x, diff_y)
    return (diff_x // com, diff_y // com)


def cmp_func(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 != x2:
        return x1 - x2
    return y1 - y2


def main():
    recs = iter(sys.stdin.readlines())
    points = []
    p_append = points.append
    n_case = int(next(recs))
    _ = next(recs)
    for tdx in range(n_case):
        while 1:
            try:
                point = next(recs).strip()
                if point:
                    p_append(list(map(int, point.split())))
                else:
                    if tdx:
                        print()
                    print(solve3(points))
                    points.clear()

            except (StopIteration):
                if len(points):
                    if tdx:
                        print()
                    print(solve3(points))
                    points.clear()
                break


if __name__ == '__main__':
    main()
