# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/124/12416.pdf
http://luckycat.kshs.kh.edu.tw/homework/q12416.htm
1 space: 0
2 spaces: 1
3 spaces: 2
4 spaces: 2
n spaces: ceil(lg(n))
"""
import bisect

def main():
    exp2s = [2**i for i in range(32)]
    while 1:
        try:
            data = input()
            space_cnt, max_spaces =0,  0

            for c in data:
                if c == ' ':
                    space_cnt += 1
                    if space_cnt > max_spaces:
                        max_spaces = space_cnt
                else:
                    space_cnt = 0
            print (bisect.bisect_left(exp2s, max_spaces))

        except (EOFError):
            break

if __name__ == '__main__':
    main()
