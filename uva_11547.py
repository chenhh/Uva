# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2542
"""

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        val = ((n*567//9+7492)*235//47)-498
        sol = (val%100)//10 if val > 0 else (-val%100)//10
        print (sol)

if __name__ == '__main__':
    main()