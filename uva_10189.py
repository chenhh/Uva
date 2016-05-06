# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/101/10189.pdf
"""

def main():
    fields = 0
    while True:
        n_row, n_col = list(map(int, input().split()))
        if n_row == 0 and n_col == 0:
            break

        mines = []
        for _ in range(n_row):
            data = input()
            mines.append(data)

        maps =[[0]*n_col for _ in range(n_row)]
        for rdx in range(n_row):
            for cdx in range(n_col):
                if mines[rdx][cdx] == '*':
                    # it is a bomb
                    maps[rdx][cdx] = '*'
                else:
                    # not a bomb
                    for r in range(max(rdx-1, 0), min(rdx+2, n_row)):
                        for c in range(max(cdx-1, 0), min(cdx+2, n_col)):
                            if mines[r][c] == '*':
                                maps[rdx][cdx] += 1
        if fields > 0:
            print ("")

        fields += 1
        print ("Field #{}:".format(fields))
        for kdx in range(n_row):
            print ("".join(str(v) for v in maps[kdx]))


if __name__ == '__main__':
    main()