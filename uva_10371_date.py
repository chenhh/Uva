# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10371.pdf

Given the current time in one time zone, you are to compute what time it is
in another time zone.
"""

zones = {
    'UTC': 0,
    'GMT': 0,
    'BST': 1,
    'IST': 1,
    'WET': 0,
    'WEST': 1,
    'CET': 1,
    'CEST': 2,
    'EET': 2,
    'EEST': 3,
    'MSK': 3,
    'MSD': 4,
    'AST': -4,
    'ADT': -3,
    'NST': -3.5,
    'NDT': -2.5,
    'EST': -5,
    'EDT': -4,
    'CST': -6,
    'CDT': -5,
    'MST': -7,
    'MDT': -6,
    'PST': -8,
    'PDT': -7,
    'HST': -10,
    'AKST': -9,
    'AKDT': -8,
    'AEST': 10,
    'AEDT': 11,
    'ACST': 9.5,
    'ACDT': 10.5,
    'AWST': 8
}


def main():
    n_case = int(input())
    for _ in range(n_case):
        curr = input().split()
        if curr[0] == 'midnight':
            base_min, src_zone, tgt_zone = 0, curr[1], curr[2]
        elif curr[0] == 'noon':
            base_min, src_zone, tgt_zone = 720, curr[1], curr[2]
        else:
            hour_min, am_pm = list(map(int, curr[0].split(':'))), curr[1]
            base_min = (hour_min[0] % 12) * 60 + hour_min[1]
            base_min += 720 if am_pm == "p.m." else 0
            src_zone, tgt_zone = curr[2:]

        tgt_base_min = int(base_min + (zones[tgt_zone] - zones[src_zone]) * 60)
        tgt_base_min %= 1440
        tgt_hour, tgt_min = divmod(tgt_base_min, 60)
        tgt_am_pm = 'a.m.' if tgt_base_min < 720 else 'p.m.'
        tgt_hour -= 12 if tgt_hour > 12 else 0

        if tgt_hour == 0 and tgt_min == 0:
            print('midnight')
        elif tgt_hour == 12 and tgt_min == 0:
            print('noon')
        else:
            print("{}:{:02d} {}".format(tgt_hour if tgt_hour else 12,
                                        tgt_min, tgt_am_pm))


if __name__ == '__main__':
    main()
