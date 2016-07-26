# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

Q147: Dollars

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/147.pdf
http://luckycat.kshs.kh.edu.tw/homework/q147.htm
"""

import sys

UPPER = 300001


def main():
    money = [0] * UPPER
    money[0] = 1
    coins = (5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000)

    for idx, coin in enumerate(coins):
        for jdx in range(coin, UPPER, 5):
            money[jdx] += money[jdx - coin]
    # print (money[:100])
    recs = iter(sys.stdin.readlines())
    while True:
        data = next(recs).strip()
        if data == '0.00':
            break

        dollar, cent = list(map(int, data.split('.')))
        print("{:3d}.{:02d}{:17d}".format(dollar, cent,
                                          money[dollar * 100 + cent]))


if __name__ == '__main__':
    main()
