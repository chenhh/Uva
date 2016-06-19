# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/167.pdf
http://luckycat.kshs.kh.edu.tw/homework/q167.htm

eight-queens problem
https://en.wikipedia.org/wiki/Eight_queens_puzzle
The possible arrangements of eight queens on an 8×8 board are 92 solutions.
"""

import sys


def queens(n_queen=8):
    """
    backtracking, searching by row first then by column.
    the size of the board is n_row * n_col (rdx from 0 to n_row -1 (n_col - 1)
    if there is a queen placed in board[rdx][cdx], then
        the rdx row, the cdx column, the diagonal (rdx+cdx)%(2*(n_col)-1), and
        the diagonal ((rdx-cdx)+(2*(n_col)-1))%((2*(n_col)-1) can't place
        another queen.

    q1: (x1, y1), q2:(x2, y2), if q1 and q2 are in the same diagonal,
    then abs( x1-x2) == abs(y1-y2)
    e.g. q1: (1, 2), then
        left diagonal :[(0,1), (2,3), (3,4), (4,5), (6,7]
        right diagonal :[(2,0), (0,3)]
        can't place another queen.

    """
    # square chessboard
    n_row = n_col = n_queen
    d_size = (2 * n_col - 1)
    ans = []

    # (rdx, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, [False] * n_col, [False] * d_size, [False] * d_size, [])]

    while stack:
        # scanning by row
        rdx, cols, lefts, rights, positions = stack.pop()
        if rdx >= n_row:
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        for cdx in range(n_col):
            l_idx, r_idx = (rdx + cdx) % d_size, (rdx - cdx) % d_size
            if not any((cols[cdx], lefts[l_idx], rights[r_idx])):
                # the position can place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = True, True, True
                stack.append((rdx + 1, cols[:], lefts[:], rights[:],
                              positions + [(rdx, cdx)]))
                # the position does not place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = False, False, False
    return ans


def main():
    n_queen = 8
    answers = queens(n_queen)
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        # 8 x 8 chess board
        board = [list(map(int, next(recs).split())) for _ in range(n_queen)]
        max_sum = max(sum(board[x][y] for x, y in pos) for pos in answers)
        print("{:>5d}".format(max_sum))


if __name__ == '__main__':
    main()
