# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/111/11136.pdf
"""


def main():
    bills = {}
    get = bills.get
    while 1:
        n_day = int(input())
        if not n_day:
            break

        bills.clear()
        pay = 0
        for _ in range(n_day):
            vals = list(map(int, input().split()))
            for val in vals[1:]:
                bills[val] = get(val, 0) + 1
            keys = bills.keys()
            max_bill, min_bill = max(keys), min(keys)
            bills[max_bill] -= 1
            if bills[max_bill] == 0:
                del bills[max_bill]

            bills[min_bill] -= 1
            if bills[min_bill] == 0:
                del bills[min_bill]
            pay += (max_bill - min_bill)
        print(pay)


if __name__ == '__main__':
    main()
