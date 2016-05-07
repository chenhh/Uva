# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/126/12611.pdf
length = R/0.2
width = 0.6 * length

upper left: (-0.45 * length,  width/2)
upper right:( 0.55 * length,  width/2)
lower right:  0.55 * length, -width/2)
lower left: (-0.45 * length, -width/2)

"""

def main():
    T = int(input())

    for tdx in range(T):
        R = int(input())
        length = int(R*5)
        left_length = int(0.45 * length)
        right_length = int(0.55 * length)
        half_width = int(0.3 * length)

        print ("Case {}:".format(tdx+1))
        print (-left_length, half_width)
        print(right_length, half_width)
        print (right_length, -half_width)
        print (-left_length, -half_width)

if __name__ == '__main__':
    main()