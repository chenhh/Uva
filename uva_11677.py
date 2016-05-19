# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/116/11677.pdf
"""

from datetime import datetime

def main():
    while 1:
        # 0<=h1, h2 <=23, 0<=m1, m2 <=59
        h1, m1, h2, m2 = list(map(int, input().split()))
        if not any((h1, m1, h2, m2)):
            break

        t1 = datetime(2016, 5, 20, h1, m1)
        t2 = datetime(2016, 5, 20, h2, m2)
        if t2 < t1:
            t2 = datetime(2016, 5, 21, h2, m2)
        diff = t2 - t1
        print (diff.seconds//60)

if __name__ == '__main__':
    main()