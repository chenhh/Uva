# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/16/1636.pdf

we have know that the gun has no bullet in the chamber (0)
what is the probability that the next chamber do not have a bullet (SHOOT)
and the probability that the chambers do not have bullets (ROTATE)

count the frequency of substring 00 is a  and 0 is b
the probability of SHOOT is a/b (given the first chamber is zero)
and the probability of ROTATE is b/n
if a/b > b/n then shoot
elif a/b < b/n then rotate
"""

import sys


def main():
    records = sys.stdin.readlines()
    for rec in records:
        bullets = rec.strip()
        zero, double_zero = 0, 0
        for idx, b in enumerate(bullets):
            if b == '0':
                zero += 1
                if bullets[(idx + 1) % len(bullets)] == '0':
                    double_zero += 1

        diff = double_zero * len(bullets) - zero * zero
        if diff == 0:
            print('EQUAL')
        elif diff > 0:
            print("SHOOT")
        else:
            print("ROTATE")


if __name__ == '__main__':
    main()
