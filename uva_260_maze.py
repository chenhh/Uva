# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/260.pdf
"""

import sys


def dfs(board, n_row):
    """
    start from (0, 0), if there is a connected components has more than
    n_row pawns, then the color wins.

    Because the game must have a winner, if the black can't join the row, then
    the while must be win.
    """
    n_col = n_row
    # lack of NE and SW
    directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]

    # find first black in 0th row
    stack = []
    for cdx, c in enumerate(board[0]):
        if c == 'b':
            stack.append((0, cdx))
            break

    if not stack:
        # no black in row 0, then white must win
        return 'W'

    while stack:
        x, y = stack.pop()
        board[x][y] = '#'
        for dx, dy in directions:
            x1, y1 = x + dx, y + dy
            if (0 <= x1 < n_row and 0 <= y1 < n_col and board[x1][y1] == 'b'):
                stack.append((x1, y1))

        if not stack:
            # for disconnected black in 0the row
            for cdx, c in enumerate(board[0]):
                if c == 'b':
                    stack.append((0, cdx))
                    break

    if '#' in board[-1]:
        # the black dfs can traversal all rows
        return 'B'
    else:
        return 'W'


def main():
    recs = iter(sys.stdin.readlines())
    case = 0
    while True:
        n_row = int(next(recs))
        if not n_row:
            break
        board = [list(next(recs).strip()) for _ in range(n_row)]
        case += 1
        ans = dfs(board, n_row)
        # print (board)
        print("{} {}".format(case, ans))


if __name__ == '__main__':
    main()
