# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    return leap


def date_shift(year, month, day, shift):
    """ uva 893
    only test for shift => 0
    but it should be worked for shift < 0
    """
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_months = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # computing base days
    pre_year, pre_month = year - 1, month - 1
    days = day + shift
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

    return (tgt_year, tgt_month + 1, days)
