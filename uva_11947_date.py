# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/119/11947.pdf
"""

from datetime import (date, timedelta)

zodiac = {
    # upper case for preventing key collision
    'CAPRICORN': ((1, 1), (1, 20)),
    'aquarius': ((1, 21), (2, 19)),
    'pisces': ((2, 20), (3, 20)),
    'aries': ((3, 21), (4, 20)),
    'taurus': ((4, 21), (5, 21)),
    "gemini": ((5, 22), (6, 21)),
    "cancer": ((6, 22), (7, 22)),
    'leo': ((7, 23), (8, 21)),
    "virgo": ((8, 22), (9, 23)),
    "libra": ((9, 24), (10, 23)),
    "scorpio": ((10, 24), (11, 22)),
    'sagittarius': ((11, 23), (12, 22)),
    # 'capricorn': ((12, 23), (1, 20))
    'capricorn': ((12, 23), (12, 31))
}


def main():
    n_case = int(input())
    for tdx in range(1, n_case + 1):
        d = input()
        month, day, year = int(d[:2]), int(d[2:4]), int(d[4:])
        birth = date(year, month, day) + timedelta(280)
        birth_zodiac = None
        for k, (s_day, e_day) in zodiac.items():
            if (date(birth.year, s_day[0], s_day[1]) <= birth <=
                    date(birth.year, e_day[0], e_day[1])):
                birth_zodiac = k.lower()
                break

        print("{} {} {}".format(tdx, birth.strftime("%m/%d/%Y"),
                                birth_zodiac))


if __name__ == '__main__':
    main()
