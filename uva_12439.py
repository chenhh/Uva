# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q12439.htm
"""


def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    return leap


def main():
    month_map = {"January": 1, "February": 2, "March": 3, "April": 4,
              "May": 5, "June": 6, "July": 7, "August": 8, "September": 9,
              "October": 10, "November": 11, "December": 12}

    T = int(input())
    for tdx in range(T):
        d1 = input().split()
        d2 = input().split()

        months = [month_map[d1[0]], month_map[d2[0]]]
        days = [int(d1[1][:-1]), int(d2[1][:-1])]
        years = [int(d1[2]), int(d2[2])]
        # print (months, days, years)
        leap_days = [0] *2

        contains = [False, True]
        for idx in range(2):
            year = years[idx]
            if is_leap(years[idx]):
                if months[idx] > 2:
                    # This year does not contain the leap day.
                    year += 1
                elif months[idx] == 2 and days[idx] == 29:
                    if contains[idx]:
                        # the end year
                        year += 1
                    else:
                        # The start year
                        year -= 1
                else:
                    # This year must contain the leap day.
                    year -= 1
            leap_days[idx] = year//4 - year//100 + year//400

        print ("Case {}: {}".format(tdx+1, leap_days[1] - leap_days[0]))

if __name__ == '__main__':
    main()
