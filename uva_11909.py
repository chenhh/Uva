# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11909.pdf

computes the volume of soya milk remaining in the packet
"""
import math

def main():
    while 1:
        try:
            # length, width, height, angle <= 90
            l, w, h, angle = list(map(int, input().split()))
            rad = angle/180 * math.pi
            h2 = l * math.tan(rad)
            if h2 <= h:
                # above the diagonal
                ans = l * w * (h - h2/2)
            else:
                # below the diagonal
                l2 = h/math.tan(rad)
                ans = l2 * w * h  / 2
            print ("{:.3f} mL".format(ans))

        except (EOFError):
            break

if __name__ == '__main__':
    main()