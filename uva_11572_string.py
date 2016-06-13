# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11572.pdf
The machine can start filling the package at any time, but once it starts,
all snowflakes flowing from the machine must go into the package until the
package is completed and sealed.

To find the longest consecutive unique numbers.
"""

import sys
from collections import defaultdict


def TLE_main():
    """unbuffer io , TLE """
    n_case = int(input())
    lastseen = defaultdict(int)

    for _ in range(n_case):
        n_snow = int(input())
        lastseen.clear()
        ans, cnt, block = 0, 0, 0
        # find the longest consecutive unique numbers
        for sdx in range(n_snow):
            snow = int(input())
            loc = lastseen[snow]
            if (loc):
                # the number has shown before
                block = max(block, loc)
                cnt = sdx - block
            cnt += 1
            lastseen[snow] = sdx + 1
            ans = max(ans, cnt)
        print(ans)


def main():
    """ buffered io, AC """
    records = iter(sys.stdin.readlines())
    n_case = int(next(records))

    lastseen = defaultdict(int)
    for _ in range(n_case):
        n_show = int(next(records))
        lastseen.clear()
        ans, cnt, block = 0, 0, 0
        for sdx in range(n_show):
            snow = int(next(records))
            loc = lastseen[snow]
            if (loc):
                # the number has shown before
                block = max(block, loc)
                cnt = sdx - block
            cnt += 1
            lastseen[snow] = sdx + 1
            ans = max(ans, cnt)
        print(ans)


if __name__ == '__main__':
    main()
