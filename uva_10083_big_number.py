# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/100/10083.pdf
"""

import sys
from math import log10


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        try:
            t, a, b = list(map(int, next(recs).split()))
            equation = "({}^{}-1)/({}^{}-1)".format(t, a, t, b)
            if t == 1:
                print("{} is not an integer with less than "
                      "100 digits.".format(equation))
            elif a == b:
                print("{} {}".format(equation, 1))
            elif a % b:
                print("{} is not an integer with less than "
                      "100 digits.".format(equation))
            elif (a - b) * log10(t) >= 100:
                print("{} is not an integer with less than "
                      "100 digits.".format(equation))
            else:
                v2 = (t ** b - 1)
                if v2 == 0:
                    # not an integer
                    print("{} is not an integer with less than "
                          "100 digits.".format(equation))
                    continue

                v1 = (t ** a - 1)
                res = str(v1 // v2)
                print("{} {}".format(equation, res))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
