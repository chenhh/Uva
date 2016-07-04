# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/112/11244.pdf
"""

import sys


def main():
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1))
    recs = iter(sys.stdin.readlines())
    stack = []
    stack_append = stack.append
    stack_pop = stack.pop
    stack_clear = stack.clear

    while True:
        n_row, n_col = list(map(int, next(recs).split()))
        if not n_row:
            break
        sky = [list(next(recs).strip()) for _ in range(n_row)]

        # find first '*'
        stack_clear()
        curr_row = 0
        star = 0
        for idx in range(n_row):
            if stack:
                break
            for jdx in range(n_col):
                if sky[idx][jdx] == '*':
                    stack_append((idx, jdx))
                    sky[idx][jdx] = '.'
                    curr_row = idx
                    star += 1
                    break
        count = 0
        while stack:
            x, y = stack_pop()
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if (0 <= x1 < n_row and 0 <= y1 < n_col and
                            sky[x1][y1] == '*'):
                    stack_append((x1, y1))
                    sky[x1][y1] = '.'
                    star += 1
            if not stack:
                if star == 1:
                    count += 1
                star = 0
                for idx in range(curr_row, n_row):
                    if stack:
                        break
                    for jdx in range(n_col):
                        if sky[idx][jdx] == '*':
                            stack_append((idx, jdx))
                            sky[idx][jdx] = '.'
                            curr_row = idx
                            star += 1
                            break
        print(count)


if __name__ == '__main__':
    main()
