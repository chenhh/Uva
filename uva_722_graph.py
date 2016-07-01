# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/722.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    n_case = int(next(recs))
    for tdx in range(n_case):
        try:
            while True:
                data = next(recs).strip()
                if data:
                    start_rdx, start_cdx = list(map(int, data.split()))
                    break

            lakes = []
            while True:
                regions = next(recs).strip()
                if regions:
                    lakes.append(list(regions))
                else:
                    raise GeneratorExit

        except (GeneratorExit, StopIteration):
            n_row, n_col = len(lakes), len(lakes[0])
            area = 1
            stack = [(start_rdx - 1, start_cdx - 1), ]
            lakes[start_rdx - 1][start_cdx - 1] = '#'
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    x1, y1 = x + dx, y + dy
                    if 0 <= x1 < n_row and 0 <= y1 < n_col and lakes[x1][
                        y1] == '0':
                        stack.append((x1, y1))
                        lakes[x1][y1] = '#'
                        area += 1
            # print (lakes)
            print(area)
            if tdx != n_case - 1:
                print()


if __name__ == '__main__':
    main()
