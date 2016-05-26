# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11586.pdf
"""


def main():
    n_case = int(input())
    for _ in range(n_case):
        pieces = input().split()
        if len(pieces) <= 1:
            print("NO LOOP")
            continue
        pieces = "".join(pieces)
        M_cnt = sum(1 for p in pieces if p == 'M')
        F_cnt = len(pieces) - M_cnt
        if M_cnt == F_cnt:
            print("LOOP")
        else:
            print("NO LOOP")


if __name__ == '__main__':
    main()
