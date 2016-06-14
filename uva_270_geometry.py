# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1

https://uva.onlinejudge.org/external/2/270.pdf

3 points in the same line (x1, y1), (x2, y2), (x3, y3)
(y2-y1)/(x2-x1) = (y3-y2)/(x3-x2), then we can get
(y2-y1) * (x3-x2) = (y3-y2)*(x2-x1)

time complexity O(n**3)
"""

import sys


def solve(points):
    # solve
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

def main():
    recs = iter(sys.stdin.readlines())
    points = []
    n_case = int(next(recs))
    _ = next(recs)
    for tdx in range(n_case):
        while 1:
            try:
                point = next(recs).strip()
                if point:
                    points.append(list(map(int, point.split())))
                else:
                    if tdx:
                        print()
                    print(solve(points))
                    points.clear()

            except (StopIteration):
                if len(points):
                    if tdx:
                        print()
                    print(solve(points))
                    points.clear()
                break


if __name__ == '__main__':
    main()
