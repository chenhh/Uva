# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


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
    diagonal_size = (2 * n_col - 1)
    ans = []

    # (rdx, cdx, rows, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, 0, [False] * n_row, [False] * n_col,
              [False] * diagonal_size, [False] * diagonal_size, [])]

    while stack:
        # column first, then by row
        rdx, cdx, rows, cols, left, right, positions = stack.pop()
        # print (rdx, cdx, queen_num)
        if rdx >= n_row:
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        if rdx < n_row and len(positions) < rdx - 1:
            # in rdx row, it should has rdx-1 or rdx queens
            # prune the impossible path
            continue

        if cdx >= n_col:
            # start from the first column of next row
            stack.append((rdx + 1, 0, rows[:], cols[:], left[:], right[:],
                          positions[:]))
            continue

        # place the queen
        l_idx = (rdx + cdx) % diagonal_size
        r_idx = (rdx - cdx + diagonal_size) % diagonal_size
        if (not rows[rdx] and not cols[cdx] and not left[l_idx]
            and not right[r_idx]):
            # the position can place a new queen
            rows[rdx], cols[cdx] = True, True
            left[l_idx], right[r_idx] = True, True

            stack.append((rdx, cdx + 1, rows[:], cols[:], left[:], right[:],
                          positions + [(rdx, cdx)]))
            rows[rdx], cols[cdx] = False, False
            left[l_idx], right[r_idx] = False, False
        # the position does not place a new queen
        stack.append((rdx, cdx + 1, rows[:], cols[:], left[:], right[:],
                      positions[:]))

    return ans


def main():
    pass


if __name__ == '__main__':
    from time import time

    t1 = time()
    ans = queens(8)
    print(len(ans), time() - t1)
