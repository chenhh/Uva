# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/117/11728.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11728.htm

S is sum of the factor of c, to find max c.
S= 102 = 101 + 1, c= 101
S = 24 = 23 + 1, c= 23
S = 36  c= 22
"""

def sum_factor(val):
    """
    sum(idx for idx in range(1, val+1) if val % idx == 0)
    """
    s = 0
    for idx in range(1, val+1):
        if val % idx == 0:
            s += idx
    return s

def main():
    sum_s = [-1] * 1001

    for idx in range(1, 1001):
        # s = sum_factor(idx)
        s = sum(jdx for jdx in range(1, idx+1) if idx % jdx == 0)
        if s <= 1000:
            sum_s[s] = idx

    cases = 0
    while 1:
        val = int(input())
        if val == 0:
            break
        cases += 1
        print ("Case {}: {}".format(cases, sum_s[val]))

if __name__ == '__main__':
    main()