# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11172.htm
"""

def main():
    N = int(input())
    for _ in range(N):
        strs = input()
        a, b = [int(v) for v in strs.split()]
        if a == b:
            print ("=")
        elif a > b:
            print (">")
        else:
            print ("<")

if __name__ == '__main__':
    main()