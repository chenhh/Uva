# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=21&page=show_problem&problem=1904
http://luckycat.kshs.kh.edu.tw/homework/q10963.htm
"""

def main():
    n = int(input())

    for ndx in range(n):
        _ = input()
        W = int(input())
        diff =[0] * W
        for idx in range(W):
            strs = input()
            y1, y2 = [int(v) for v in strs.split()]
            diff[idx] = y1 - y2

        sol = True
        for idx in range(1, W):
            if diff[idx] != diff[idx-1]:
                sol = False
                break
        print ("{}".format("yes" if sol else "no"))

        if ndx != n-1:
            print ("")

if __name__ == '__main__':
    main()