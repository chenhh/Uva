# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10946.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    case = 0
    while True:
        n_row, n_char = list(map(int, next(recs).split()))
        if not n_row:
            break
        roads = [list(next(recs).strip()) for _ in range(n_row)]
        n_col = len(roads[0])
        stack, holes = [], []
        alphabet, area = None, 0
        for rdx in range(n_row):
            if area:
                break
            for cdx in range(n_col):
                if roads[rdx][cdx] != '.':
                    alphabet = roads[rdx][cdx]
                    stack.append((rdx, cdx))
                    roads[rdx][cdx] = '.'
                    area += 1
                    break

        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if (0 <= x1 < n_row and 0 <= y1 < n_col and
                            roads[x1][y1] == alphabet):
                    stack.append((x1, y1))
                    roads[x1][y1] = '.'
                    area += 1

            if not stack:
                holes.append((alphabet, area))
                alphabet, area = None, 0
                for rdx in range(n_row):
                    if area:
                        break
                    for cdx in range(n_col):
                        if roads[rdx][cdx] != '.':
                            alphabet = roads[rdx][cdx]
                            stack.append((rdx, cdx))
                            roads[rdx][cdx] = '.'
                            area += 1
                            break
        case += 1
        holes.sort(key=lambda x: (-x[1], x[0]))
        print("Problem {}:".format(case))
        for c, v in holes:
            print("{} {}".format(c, v))


if __name__ == '__main__':
    main()
