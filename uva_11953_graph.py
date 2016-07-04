# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/119/11953.pdf
"""

import sys


def main():
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    stack = []
    stack_append = stack.append
    stack_pop = stack.pop

    for tdx in range(n_case):
        n_size = int(next(recs))
        map = [list(next(recs).strip()) for _ in range(n_size)]

        n_ship = 0
        stack.clear()
        curr_row = 0
        # find first 'x'
        for idx in range(n_size):
            if stack:
                break
            for jdx in range(n_size):
                if map[idx][jdx] == 'x':
                    stack_append((idx, jdx))
                    map[idx][jdx] = '#'
                    curr_row = idx
                    n_ship += 1
                    break

        while stack:
            x, y = stack_pop()
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if (0 <= x1 < n_size and 0 <= y1 < n_size and
                            map[x1][y1] in ('x', '@')):
                    stack_append((x1, y1))
                    map[x1][y1] = '#'

            if not stack:
                for idx in range(curr_row, n_size):
                    if stack:
                        break
                    for jdx in range(n_size):
                        if map[idx][jdx] == 'x':
                            stack_append((idx, jdx))
                            map[idx][jdx] = '#'
                            curr_row = idx
                            n_ship += 1
                            break

        print("Case {}: {}".format(tdx + 1, n_ship))


if __name__ == '__main__':
    main()
