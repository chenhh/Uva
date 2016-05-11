# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11494.htm

upper left: (1, 1), upper right: (1, 8)
lower left: (8, 1), lower right(: (8, 8)
(row, col): (X, Y)
The queen  moving to any position on the board requires at most 2 steps.
"""

def main():
    while 1:
        x1, y1, x2, y2 = list(map(int, input().split()))
        if x1 == 0 and y1 ==0 and x2 ==0 and y2 == 0:
            break

        if x1 == x2 and y1 == y2:
            # the same start and end position
            print (0)
        elif x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
            # the same vertical line or horizontal line or diagonal direction
            print (1)
        else:
            print (2)

if __name__ == '__main__':
    main()

