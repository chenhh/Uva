# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/128/12894.pdf
"""

EPS = 1e-3


def main():
    T = int(input())
    for _ in range(T):
        x0, y0, x1, y1, cx, cy, r = list(map(int, input().split()))

        valid = True
        length = x1 - x0
        width = y1 - y0
        if length <= 0 or width <= 0:
            valid = False
        elif abs(width / length - 0.6) > EPS:
            # width: length = 6: 10
            valid = False
        elif abs(length / r - 5) > EPS:
            # length: radius = 5: 1
            valid = False
        elif abs(cy - (y0 + y1) / 2) > EPS:
            # circle center in the middle of width
            valid = False
        elif abs(cx - x0 - 0.45 * length) > EPS:
            # circle center in the 45th of length
            valid = False

        # print (width/length, length/r,
        #        abs(cy - (y0+y1)/2), abs(cx - x0 - 0.45*length) )
        print("YES" if valid else "NO")


if __name__ == '__main__':
    main()
