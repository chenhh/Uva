# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/131/13115.pdf
"""

import sys

sqrt_roots = {idx * idx: idx for idx in range(1, 6)}


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        n_size = int(next(recs))
        n_sub_size = sqrt_roots[n_size]

        sudoku = [list(map(int, next(recs).split())) for _ in range(n_size)]

        correct = True
        # check row
        for idx in range(n_size):
            row = frozenset(sudoku[idx][jdx] for jdx in range(n_size))
            if len(row) != n_size:
                correct = False
                break

        if correct:
            for jdx in range(n_size):
                col = frozenset(sudoku[idx][jdx] for idx in range(n_size))
                if len(col) != n_size:
                    correct = False
                    break

        # check sub-regions
        if correct:
            for idx in range(0, n_size, n_sub_size):
                if not correct:
                    break
                for jdx in range(0, n_size, n_sub_size):
                    # block = idx + (jdx//n_sub_size)
                    sub_regions = frozenset(sudoku[kdx][ldx]
                                            for kdx in
                                            range(idx, idx + n_sub_size)
                                            for ldx in
                                            range(jdx, jdx + n_sub_size))
                    if len(sub_regions) != n_size:
                        correct = False
                        break
        print("yes" if correct else "no")


if __name__ == '__main__':
    main()
