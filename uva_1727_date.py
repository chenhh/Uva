# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/17/1727.pdf
"""

months = {
    "JAN": 31, "FEB": 28, "MAR": 31, "APR": 30, 'MAY': 31, 'JUN': 30,
    'JUL': 31, 'AUG': 31, 'SEP': 30, 'OCT': 31, 'NOV': 30, 'DEC': 31,
}

weekdays = {
    'SUN': 7, 'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6
}


def main():
    n_case = int(input())
    for _ in range(n_case):
        # assume the year is not a leap year
        month, first_day = list(input().split())
        ans = sum(1 if (weekdays[first_day] + idx) % 7 in (5, 6) else 0
                  for idx in range(months[month]))
        print(ans)


if __name__ == '__main__':
    main()
