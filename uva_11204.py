# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11204.htm
Dispatching N instruments to M students.
"""
from functools import reduce

def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        instruments = [0] * N

        # rank
        for idx in range(M):
            ranks = list(map(int, input().split()))
            for rdx, rank in enumerate(ranks):
                if rank == 1:
                    # each student has only one rank 1 instrument
                    instruments[rdx] += 1
                    break

        # product of all non-zero elements
        print (reduce(lambda x,y: x*y, [v for v in instruments if v > 0]))

if __name__ == '__main__':
    main()