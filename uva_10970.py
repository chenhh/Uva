# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/109/10970.pdf

Cutting the row first, then cut the column. 
It requires (r-1) * (c-1)* r = r*c -1 cuts.

Cutting the column first, then cut the row. 
It requires (c-1) * (r-1)* c = r*c -1 cuts.
"""

def main():
    while 1:
        try:
            M, N = list(map(int, input().split()))
            print (M * N -1)
        except (EOFError):
            break
            
if __name__ == '__main__':
    main()
    