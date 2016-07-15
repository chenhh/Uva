# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10339.pdf
"""

import sys


def main():
    one_round = 12 * 60 * 60
    one_day = 24 * 60 * 60

    recs = sys.stdin.readlines()

    for rec in recs:
        # 0<=k,m <=256, the number of seconds per day that each watch loses
        k, m = list(map(int, rec.split()))
        diff = abs(k - m)
        if not diff:
            print("{} {} 12:00".format(k, m))
            continue

        # how many rounds to get the correct time
        period = one_round / diff
        t = int(period * (one_day - k) / 60 + 0.5) % one_day
        h = (t // 60) % 12
        h = 12 if not h else h
        f = t % 60
        print("{} {} {:02d}:{:02d}".format(k, m, h, f))


if __name__ == '__main__':
    main()
