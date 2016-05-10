# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11579.htm

Heron formula:
area = sqrt(s*(s-a)*(s-b)*(s-c)), s=(a+b+c)/2

assuming a<=b<=c, three edges can't form a triangle if a+b <= c
"""
import math

def main():
    T = int(input())

    for _ in range(T):
        data = list(map(float, input().split()))
        N, edges = int(data[0]), sorted(data[1:])

        # triangle
        areas = [0,]
        for ndx in range(N-1, 1, -1):
            c = edges[ndx]
            a, b = edges[ndx-2], edges[ndx-1]
            if a+b > c:
                s = (a+b+c)/2
                areas.append(math.sqrt(s*(s-a)*(s-b)*(s-c)))

        print ("{:.2f}".format(max(areas)))

if __name__ == '__main__':
    main()

