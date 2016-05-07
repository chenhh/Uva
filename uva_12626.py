# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/126/12626.pdf

MARGARITA: M:1, A:3, R:2, G:1, I:1, T:1
"""
from collections import Counter

def main():
    pizza = {'M':1, 'A':3, 'R':2, 'G':1, 'I':1, 'T':1}
    N = int(input())

    for _ in range(N):
        alphas = input().strip()
        ctr = Counter(alphas)

        num = 0
        finished = False
        while not finished:
            for k, v in pizza.items():
                ctr[k] -= v
                if ctr[k] < 0:
                    finished = True
                    break
            if not finished:
                num += 1
        print (num)

if __name__ == '__main__':
    main()



