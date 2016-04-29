# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1753
http://luckycat.kshs.kh.edu.tw/homework/q10812.htm
"""

def main():
    N = int(input())
    for _ in range(N):
        strs = input()
        s, d = [int(v) for v in strs.split()]

        sol = True
        # s = a+b, d= (a-b), a, b>0
        if (s+d) %2 == 1 or d > s:
            sol = False
        else:
            a = (s+d)//2
            b = s-a
            if b < 0:
                sol = False
        if sol:
            print ("{} {}".format(a, b))
        else:
            print ("impossible")

if __name__ == '__main__':
    main()