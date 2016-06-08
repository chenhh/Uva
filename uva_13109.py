# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/131/13109.pdf

greedy method
"""


def main():
    n_case = int(input())
    for _ in range(n_case):
        n_elephant, max_weight = list(map(int, input().split()))
        weights = sorted(list(map(int, input().split())))
        cum_weight, count = 0, 0
        for idx, weight in enumerate(weights):
            cum_weight += weight
            if cum_weight <= max_weight:
                count += 1
            else:
                break
        print(count)


if __name__ == '__main__':
    main()
