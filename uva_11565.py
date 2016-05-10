# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11565.htm
1 <= a, b, c <= 10000
x+y+z=a
xyz=b
x^2+y^2+z^2=c
"""

def main():
    N = int(input())

    for _ in range(N):
        a, b, c = list(map(int, input().split()))
