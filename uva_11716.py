# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/117/11716.pdf
"""

def decrypt(code, n_row):
    """ matrix from row major to column major """
    output = [code[rdx *n_row+cdx]
              for cdx in range(n_row)
              for rdx in range(n_row)]
    return "".join(output)

def main():
    # Total number of character in the text will not be more 10,000.
    square = {}
    for x in range(100+1):
        square[x*x] = x

    T = int(input())
    for _ in range(T):
        code = input()

        len_code = len(code)
        if len_code in square.keys():
            print(decrypt(code, square[len_code]))
        else:
            print("INVALID")

if __name__ == '__main__':
    main()