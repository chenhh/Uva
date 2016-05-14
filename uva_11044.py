# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/110/11044.pdf
"""

def main():
    T = int(input())
    for _ in range(T):
        n, m = list(map(int, input().split()))
        n_row, n_col =n//3, m//3
        print (n_row * n_col)

if __name__ == '__main__':
    main()