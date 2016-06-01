# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/113/11308.pdf
"""

from collections import defaultdict


def main():
    n_binder = int(input())

    for _ in range(n_binder):
        binder_name = input().strip()
        n_ingredient, n_receipt, budget = list(map(int, input().split()))

        prices = defaultdict(int)
        for _ in range(n_ingredient):
            ingredient, price = input().split()
            prices[ingredient] = int(price)

        costs = defaultdict(int)
        for _ in range(n_receipt):
            receipt_name = input().strip()
            costs[receipt_name] = 0

            k = int(input())
            for _ in range(k):
                ingredient, requirement = input().split()
                costs[receipt_name] += prices[ingredient] * int(requirement)

        # print
        print(binder_name.upper())
        # sort by cost first (ascending) then by cake name
        sorted_data = sorted(costs.items(), key=lambda k: (k[1], k[0]))
        if sorted_data[0][1] > budget:
            print("Too expensive!")
        else:
            for name, cost in sorted_data:
                if cost <= budget:
                    print(name)
        print()


if __name__ == '__main__':
    main()
