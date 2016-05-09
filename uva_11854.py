# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/118/11854.pdf
"""

def main():
    while 1:
        data = list(map(int, input().split()))
        if data[0] == 0 and data[1] == 0 and data[2] == 0:
            break

        edges2 = sorted([v*v for v in data])
        if edges2[0] + edges2[1] == edges2[2]:
            print ('right')
        else:
            print ('wrong')

if __name__ == '__main__':
    main()