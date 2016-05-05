# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/116/11636.pdf

2**(Y-1)< N <= 2**Y
given N to find Y

0 < N < 10001
Y=0 ~ 14
"""
import bisect

def main():
    exps = [2**idx for idx in range(15)]
    idx = 0

    while True:
        N = int(input())
        if N < 0:
            break
        else:
            idx += 1
            Y = bisect.bisect_left(exps, N)
            print ("Case {}: {}".format(idx, Y))

if __name__ == '__main__':
    main()