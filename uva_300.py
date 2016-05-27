# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/3/300.pdf
http://luckycat.kshs.kh.edu.tw/homework/q300.htm
"""

# 365 days a year, 20 days in month 0-17 and 5 days in month 18
Haab_month = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol',
              'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax',
              'koyab', 'cumhu', 'uayet']
# 260 days a year
Tzolkin_day = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik',
               'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem',
               'cib', 'caban', 'eznab', 'canac', 'ahau']

Tzolkin_calendar = [((day % 13) + 1, Tzolkin_day[day % 20]) for day in
                    range(260)]


def main():
    n_case = int(input())
    print(n_case)

    for idx in range(n_case):
        # Haab format: NumberOfTheDay. Month Year
        Haabs = input().split()
        h_day = int(Haabs[0][:Haabs[0].rfind('.')])
        h_month = Haab_month.index(Haabs[1])
        h_year = int(Haabs[2])
        h_value = h_year * 365 + h_month * 20 + h_day

        # Tzolkin format: Number NameOfTheDay Year
        t_year, res = divmod(h_value, 260)
        t_value = Tzolkin_calendar[res]
        print("{} {} {}".format(t_value[0], t_value[1], t_year))


if __name__ == '__main__':
    main()
