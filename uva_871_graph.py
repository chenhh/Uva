# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/8/871.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1),
                  (-1, 1), (-1, -1))

    n_case = int(next(recs))
    _ = next(recs)
    for tdx in range(n_case):
        try:
            figure = []
            while True:
                row = next(recs).strip()
                if row:
                    figure.append(list(row))
                else:
                    raise GeneratorExit

        except (GeneratorExit, StopIteration):
            n_row, n_col = len(figure), len(figure[0])
            stack = []
            area, max_area = 0, 0
            for rdx in range(n_row):
                if area:
                    break
                for cdx in range(n_col):
                    if figure[rdx][cdx] == '1':
                        stack.append((rdx, cdx))
                        figure[rdx][cdx] = '#'
                        max_area = area = 1
                        break

            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    x1, y1 = x + dx, y + dy
                    if (0 <= x1 < n_row and 0 <= y1 < n_col and
                                figure[x1][y1] == '1'):
                        stack.append((x1, y1))
                        figure[x1][y1] = '#'
                        area += 1

                if not stack:
                    if area > max_area:
                        max_area = area
                    area = 0
                    for rdx in range(n_row):
                        if area:
                            break
                        for cdx in range(n_col):
                            if figure[rdx][cdx] == '1':
                                stack.append((rdx, cdx))
                                figure[rdx][cdx] = '#'
                                area += 1
                                break
            # print (n_row, n_col)
            # print (figure)
            print(max_area)
            if tdx != n_case - 1:
                print()


if __name__ == '__main__':
    main()
