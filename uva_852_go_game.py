# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/8/852.pdf
"""

import sys
from collections import deque
from itertools import product


def main():
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    n_row, n_col = 9, 9
    positions = list(product(range(n_row), range(n_col)))

    stack = deque()
    stack_append = stack.append
    stack_pop = stack.pop
    stack_clear = stack.clear
    for _ in range(n_case):
        board = [next(recs).strip() for _ in range(n_row)]
        # 0: not visited, 1: visited by white, 2: visited by black
        # 3: overlap
        visited = [[0] * n_col for _ in range(n_row)]

        stack_clear()
        # white areas
        white_area = 0
        for x, y in positions:
            if board[x][y] == 'O':
                stack_append((x, y))
                visited[x][y] = 1
                white_area += 1

        while stack:
            x, y = stack_pop()
            for dx, dy in directions:
                x1 = x + dx
                y1 = y + dy
                if (0 <= x1 < 9 and 0 <= y1 < 9 and not visited[x1][y1] and
                            board[x1][y1] == '.'):
                    # greedy visit, without considering overlap
                    stack_append((x1, y1))
                    visited[x1][y1] = 1
                    white_area += 1

        # print ("white visited")
        # print (visited)

        # black areas
        black_area = 0
        for x, y in positions:
            if board[x][y] == 'X':
                stack_append((x, y))
                visited[x][y] = 2
                black_area += 1

        over_lap = 0
        while stack:
            x, y = stack_pop()
            for dx, dy in directions:
                x1 = x + dx
                y1 = y + dy
                if (0 <= x1 < 9 and 0 <= y1 < 9 and board[x1][y1] == '.'):
                    if visited[x1][y1] != 2:
                        stack_append((x1, y1))
                        black_area += 1
                        if visited[x1][y1] == 1:
                            # empty pos, but it was visited by white
                            # print("overlap:", x1, y1)
                            over_lap += 1
                        visited[x1][y1] = 2

        white_area -= over_lap
        black_area -= over_lap
        print("Black {} White {}".format(black_area, white_area))


if __name__ == '__main__':
    main()
