# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/112/11292.pdf
"""


def main():
    while 1:
        n_head, n_knight = list(map(int, input().split()))
        if n_head == 0:
            break
        diameters = [int(input()) for _ in range(n_head)]
        heights = [int(input()) for _ in range(n_knight)]

        # Each knight can chop off one of the dragon’s heads.
        if n_knight < n_head:
            print("Loowater is doomed!")
            continue

        diameters.sort()
        heights.sort()
        coin = 0
        sdx, hdx = 0, 0
        while sdx < n_head and hdx < n_knight:
            if diameters[sdx] <= heights[hdx]:
                coin += heights[hdx]
                sdx += 1
                hdx += 1
            else:
                hdx += 1
        if sdx != n_head:
            print("Loowater is doomed!")
        else:
            print(coin)


if __name__ == '__main__':
    main()
