# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/7/750.pdf
the input format in the html and pdf are wrong,
and input format in iDebug are correct.
"""

import sys


def queens_with_a_fixed_position(x, y, n_queen=8):
    """
    backtracking, searching by row first then by column.
    the size of the board is n_row * n_col (rdx from 0 to n_row -1 (n_col - 1)
    if there is a queen placed in board[rdx][cdx], then
        the rdx row, the cdx column, the diagonal (rdx+cdx)%(2*(n_col)-1), and
        the diagonal ((rdx-cdx)+(2*(n_col)-1))%((2*(n_col)-1) can't place
        another queen.

    x, y is the location of a given queen.
    """
    # square chessboard
    n_row = n_col = n_queen
    d_size = (2 * n_col - 1)
    ans = []

    # initial condition
    i_cols = [False] * n_col
    i_cols[y] = True
    i_lefts, i_rights = [False] * d_size, [False] * d_size
    i_lefts[(x + y) % d_size], i_rights[(x - y) % d_size] = True, True

    # (rdx, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, i_cols, i_lefts, i_rights, [(x, y)])]

    while stack:
        rdx, cols, lefts, rights, positions = stack.pop()
        # print (rdx, cols, positions)
        if rdx >= n_row:
            # because the xth row will not be checked, there are only
            # n_row -1 rows need to be checked
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        if rdx == x:
            stack.append((rdx + 1, cols[:], lefts[:], rights[:],
                          positions[:]))
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
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for cdx in range(n_case):
        _ = next(recs)
        x, y = list(map(int, next(recs).split()))
        ans = queens_with_a_fixed_position(x - 1, y - 1)
        ans_by_cols = sorted(" ".join(str(x + 1) for x, _ in
                                      sorted(pos, key=lambda x: x[1]))
                             for pos in ans)
        if cdx:
            print()
        print("SOLN       COLUMN")
        print(" #      1 2 3 4 5 6 7 8")
        print()
        for rdx, row in enumerate(ans_by_cols):
            print("{:>2d}      {}".format(rdx + 1, row))


if __name__ == '__main__':
    main()
