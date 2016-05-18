# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1
https://uva.onlinejudge.org/external/119/11900.pdf

conditions:
-------------------------
n eggs and a bowl
It’s risky to put more than P eggs in the bowl
the bowl can carry at most Q gm of eggs
you are given the weight of the eggs in gm
You have to find the maximum number of eggs they can boil without taking
any risk
"""


def main():
    T = int(input())
    for tdx in range(T):
        n, P, Q = list(map(int, input().split()))
        # the weights of n eggs, in non-descending order
        weights = list(map(int, input().split()))

        count = 0
        egg_weight = 0
        while count < min(n, P):
            if egg_weight + weights[count] <= Q:
                egg_weight += weights[count]
                count += 1
            else:
                break

        print("Case {}: {}".format(tdx + 1, count))


if __name__ == '__main__':
    main()
