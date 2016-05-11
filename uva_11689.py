# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/116/11689.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11689.htm
"""

def main():
    N = int(input())

    for _ in range(N):
        e, f, c = list(map(int, input().split()))

        current = e+f
        soda = 0
        while current >= c:
            changes = current // c
            remains = current % c
            soda += changes
            current = changes + remains
        print (soda)

if __name__ == '__main__':
    main()
