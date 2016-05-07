# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/125/12578.pdf
rectangle: L * 0.6L
red pi * r^2 = pi * (0.2L)**2 = 0.04*L**L * pi
green: 0.6*L*L - red

"""
import math

def main():
    T = int(input())

    for _ in range(T):
        L = int(input())
        L2 = L * L
        red = 0.04*L2*math.pi
        green = 0.6*L2 - red
        print ("{:.2f} {:.2f}".format(red, green))

if __name__ == '__main__':
    main()