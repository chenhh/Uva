# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/8/893.pdf
"""

months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
leap_months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap(year):
    return (True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0
            else False)


def main():
    while 1:
        # n_ahead, day, month, year
        values = list(map(int, input().split()))
        if not any(values):
            break
        n_ahead, day, month, year = values

        # computing base days
        pre_year, pre_month = year - 1, month - 1
        days = day + n_ahead
        days += (pre_year * 365 + pre_year // 4 - pre_year // 100 +
                 pre_year // 400)
        days += sum(months[mdx] for mdx in range(pre_month))
        days += 1 if is_leap(year) and pre_month >= 2 else 0

        tgt_year = days // 366
        tgt_days = (tgt_year * 365 + tgt_year // 4 - tgt_year // 100 +
                    tgt_year // 400)
        # find tgt_year base_days < days <= (tgt_year+1) base_days
        while tgt_days < days:
            tgt_year += 1
            tgt_days = (tgt_year * 365 + tgt_year // 4 - tgt_year // 100 +
                        tgt_year // 400)

        days -= tgt_days
        days += 366 if is_leap(tgt_year) else 365

        cur_months = leap_months if is_leap(tgt_year) else months
        tgt_month = 0
        while days > cur_months[tgt_month]:
            days -= cur_months[tgt_month]
            tgt_month += 1

        print(days, tgt_month + 1, tgt_year)


if __name__ == '__main__':
    main()
