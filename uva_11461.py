# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

11461 Square Numbers
https://uva.onlinejudge.org/external/114/11461.pdf
316**2 =99856
317**2 = 100489
"""
import bisect

def main():
    squares = [val**2 for val in range(1, 318)]

    while True:
        # 0 < a <=1e5
        a, b = list(map(int, input().split()))
        if a == 0 and b == 0:
            break
        sdx = bisect.bisect_left(squares, a)
        edx = bisect.bisect_right(squares, b)
        print (edx-sdx)

if __name__ == '__main__':
    main()