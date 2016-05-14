# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/2/299.pdf

the number of swap in the bubble sort
"""

def main():
    N = int(input())
    for _ in range(N):
        L = int(input())
        trains = list(map(int, input().split()))

        swap = 0
        for idx in range(L):
            for jdx in range(idx+1, L):
                if trains[idx] > trains[jdx]:
                    swap += 1
                    trains[idx], trains[jdx] = trains[jdx], trains[idx]

        print ("Optimal train swapping takes {} swaps.".format(swap))

if __name__ == '__main__':
    main()
