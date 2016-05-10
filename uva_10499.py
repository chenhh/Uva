# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/104/10499.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10499.htm

sphere surface area: 4*pi*r^2
area of circle: pi*r^2 (25% profit)
2 equal pieces, the surface area will increase 2  circles (50% profit)
3 equal pieces, the surface area will increase 3 circles (75% profit)
4 equal pieces, the surface area will increase 4 circles (100% profit)
"""

def main():
    while 1:
        n = int(input())
        if n < 0:
            break
        if n == 1:
            profit = 0
        else:
            profit = n*25.0
        print ("{:.0f}%".format(profit))

if __name__ == '__main__':
    main()
