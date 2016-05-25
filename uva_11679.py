# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/116/11679.pdf
"""


def main():
    while 1:
        n_bank, n_debenture = list(map(int, input().split()))
        if n_bank == 0 and n_debenture == 0:
            break
        owns = list(map(int, input().split()))

        for _ in range(n_debenture):
            owe, owed, amount = list(map(int, input().split()))
            owns[owe - 1] -= amount
            owns[owed - 1] += amount

        possible = True
        for own in owns:
            if own < 0:
                possible = False
                break
        print("S" if possible else "N")


if __name__ == '__main__':
    main()
