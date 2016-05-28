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


def time_zone(hour, min, am_pm, src_zone, tgt_zone):
    """ uva 10371 """
    zones = {
        'UTC': 0, 'GMT': 0, 'BST': 1, 'IST': 1, 'WET': 0, 'WEST': 1,
        'CET': 1, 'CEST': 2, 'EET': 2, 'EEST': 3, 'MSK': 3, 'MSD': 4,
        'AST': -4, 'ADT': -3, 'NST': -3.5, 'NDT': -2.5, 'EST': -5, 'EDT': -4,
        'CST': -6, 'CDT': -5, 'MST': -7, 'MDT': -6, 'PST': -8, 'PDT': -7,
        'HST': -10, 'AKST': -9, 'AKDT': -8, 'AEST': 10, 'AEDT': 11,
        'ACST': 9.5, 'ACDT': 10.5, 'AWST': 8
    }

    base_min = (hour % 12) * 60 + min
    base_min += 720 if am_pm == "p.m." else 0
    tgt_base_min = int(base_min + (zones[tgt_zone] - zones[src_zone]) * 60)
    tgt_base_min %= 1440
    tgt_hour, tgt_min = divmod(tgt_base_min, 60)
    tgt_am_pm = 'a.m.' if tgt_base_min < 720 else 'p.m.'
    tgt_hour -= 12 if tgt_hour > 12 else 0
    return (tgt_hour if tgt_hour else 12, tgt_min, tgt_am_pm)
