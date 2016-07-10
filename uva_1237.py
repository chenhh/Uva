# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/12/1237.pdf
"""

import sys
from bisect import (bisect_right)


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for tdx in range(n_case):
        n_car = int(next(recs))
        car_prices = []
        for _ in range(n_car):
            car, low, high = next(recs).split()
            car_prices.append((car, int(low), int(high)))

        # 1st: low price, 2nd: high price
        car_prices.sort(key=lambda x: (x[1], x[2]))
        cars, lows, highs = zip(*car_prices)
        # print (car_prices)
        n_query = int(next(recs))
        for _ in range(n_query):
            price = int(next(recs))
            cnt = 0
            car = None
            # the index which the price is larger than the low price.
            edx = bisect_right(lows, price)
            # sdx = bisect_right(highs, price)
            for cdx in range(0, edx):
                if lows[cdx] <= price <= highs[cdx]:
                    cnt += 1
                    car = cars[cdx]
                if cnt > 1:
                    break
            if cnt == 1:
                print(car)
            else:
                print("UNDETERMINED")

        if tdx != n_case - 1:
            print()


if __name__ == '__main__':
    main()
