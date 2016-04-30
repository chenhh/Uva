# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11356.htm
"""

from datetime import (date, timedelta)

def main():
    month_dict = {"January":1, "February": 2, "March": 3, "April": 4,
                  "May": 5, "June": 6, "July":7, "August": 8, "September":9,
                  "October": 10, "November": 11, "December":12}
    month_str = sorted(month_dict, key=month_dict.get)

    cnt = int(input())
    for idx in range(cnt):
        starts = input().split('-')
        shift = int(input())

        today = date(int(starts[0]), month_dict[starts[1]], int(starts[2]))
        next = today + timedelta(shift)
        print ("Case {}: {}-{}-{:02d}".format(idx+1, next.year,
                                              month_str[next.month-1],
                                              next.day))

if __name__ == '__main__':
    main()