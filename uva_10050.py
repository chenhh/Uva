# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/100/10050.pdf
"""

def main():
    T = int(input())
    for _ in range(T):
        # simulation days
        N = int(input())
        hartels = [0] * N

        # number of parties
        P = int(input())
        for pdx in range(P):
            number = int(input())

            for ndx in range(N):
                fri, sat = (ndx+2) %7, (ndx+1) % 7
                if fri !=0 and sat != 0 and (ndx+1)%number == 0:
                    hartels[ndx] = 1

        print (sum(hartels))

if __name__ == '__main__':
    main()