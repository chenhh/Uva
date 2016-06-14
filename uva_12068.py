# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/120/12068.pdf
using python fractions.Fraction will get WA

h4 = 4/(1/a+1/b+1/c+1/d) = 4/((bcd+acd+abd+abc)/(abcd))
   = 4*abcd/(bcd+acd+abd+abc)
"""

import operator
import sys
from functools import reduce


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for tdx in range(n_case):
        data = list(map(int, next(recs).split()))
        n, vals = data[0], data[1:]
        denominator = reduce(operator.mul, vals)
        numerator = denominator * n
        denominator = sum(denominator // v for v in vals)
        tmp = gcd(numerator, denominator)
        print("Case {}: {}/{}".format(
            tdx + 1, numerator // tmp, denominator // tmp))


if __name__ == '__main__':
    main()
