# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/104/10433.pdf

Sample Input
5
76
34
0081787109376
1
0

Sample Output
Automorphic number of 1-digit.
Automorphic number of 2-digit.
Not an Automorphic number.
Automorphic number of 13-digit.
Not an Automorphic number.
Not an Automorphic number.
"""

import sys


def main():
    records = sys.stdin.readlines()

    for rec in records:
        # the records may contain negative numbers
        # Some Automorphic number have leading zeros. So leading
        # zeros must be considered as significant.
        line = rec.strip()
        data_len = len(line)
        value = int(line)

        if value in (0, 1):
            print("Not an Automorphic number.")
            continue

        value_square = str(value * value)
        if str(line) == value_square[-data_len:]:
            print("Automorphic number of {}-digit.".format(data_len))
        else:
            print("Not an Automorphic number.")


if __name__ == '__main__':
    main()
