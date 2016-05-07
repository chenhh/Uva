# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/113/11340.pdf
"""

def main():
    N = int(input())

    for ndx in range(N):
        K = int(input())

        values = {}
        for kdx in range(K):
            c, v = input().split()
            values[c] = int(v)

        M = int(input())
        pay = 0
        for mdx in range(M):
            line = input()
            pay += sum(values[d] for d in line if d in values.keys())

        print ("{:.2f}$".format(pay/100))

if __name__ == '__main__':
    main()



