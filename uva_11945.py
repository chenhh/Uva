# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11945.pdf
"""

def main():
    N = int(input())

    for ndx in range (N):
        account = 0
        for _ in range(12):
            value = float(input())
            account += value
        print ("{} ${:,.2f}".format(ndx+1, account/12))

if __name__ == '__main__':
    main()