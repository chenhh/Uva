# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=18&page=show_problem&problem=1637
http://luckycat.kshs.kh.edu.tw/homework/q10696.htm
"""
MAX=1000001

cache = [0] * MAX

def f91(n):
    if n<=MAX and cache[n] != 0:
        return cache[n]



def main():
    while True:
        val = input()
        n = int(val)
        if n == 0:
            break



if __name__ == '__main__':
    main()