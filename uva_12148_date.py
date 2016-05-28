# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/121/12148.pdf
"""

from datetime import (date, timedelta)


def main():
    while 1:
        n_record = int(input())
        if not n_record:
            break

        prev_date, prev_c, cnt, consumption = None, 0, 0, 0
        for _ in range(n_record):
            d, m, y, c = list(map(int, input().split()))
            today = date(y, m, d)
            if prev_date == today - timedelta(1):
                consumption += (c - prev_c)
                cnt += 1
            prev_date = today
            prev_c = c
        print("{} {}".format(cnt, consumption))


if __name__ == '__main__':
    main()
