# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/400.pdf
"""

MAX_COL = 60


def main():
    while 1:
        try:
            n_file = int(input())
            # you will sort (ascending based on the ASCII character values)
            # and format into (C) columns based on the length (L) of the
            # longest name.
            file_names = sorted(input().strip() for _ in range(n_file))
            # print(file_names)

            # The rightmost column will be the width of the longest filename
            # and all other columns will be the width of the longest filename
            # plus 2.
            max_len = max(len(name) for name in file_names)
            n_col = (MAX_COL - max_len) // (max_len + 2) + 1
            n_row = (n_file - 1) // n_col + 1
            # print (n_row, n_col, max_len)

            print('-' * MAX_COL)
            # column major
            for rdx in range(n_row):
                for cdx in range(n_col):
                    idx = rdx + cdx * n_row
                    if idx < n_file:
                        if cdx != n_col - 1:
                            print("{0:<{1}}".format(
                                file_names[idx], max_len + 2), end="")
                        else:
                            print("{0:<{1}}".format(
                                file_names[idx], max_len), end="")
                print()

        except (EOFError):
            break


if __name__ == '__main__':
    main()
