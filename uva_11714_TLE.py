# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11714.htm
https://uva.onlinejudge.org/external/117/11714.pdf

the largest number: (n-1)
the second largest number: floor(log_2(n-1))
"""

import bisect

def main():
    exp2 = [2**idx for idx in range(38)]

    while 1:
        try:
            n = int(input())
            # TLE version
            # tle = ((n-1)+int(math.log2(n-1)))
            idx = bisect.bisect_left(exp2, n-1)
            if exp2[idx] > (n-1):
                idx -=1
            print ((n-1)+ idx)

        except (EOFError):
            break

if __name__ == '__main__':
    main()

