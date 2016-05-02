# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2
http://luckycat.kshs.kh.edu.tw/homework/q12405.htm
greedy
find the leftmost fertile field (idx),
 place a crow in the next location (idx+1),
then the (idx, idx+1, idx+2) is protected.
Continue the search from idx+3
"""

import math

def main():
    T = int(input())
    for tdx in range(T):
        N = int(input())
        fields = list(input())

        crow = 0
        for idx in range(N):
            if fields[idx] == '.':
                crow += 1
                if idx+1 <= N-1:
                    fields[idx+1] = '#'
                if idx + 2 <= N - 1:
                    fields[idx + 2] = '#'
        print ("Case {}: {}".format(tdx+1, crow))


if __name__ == '__main__':
    main()