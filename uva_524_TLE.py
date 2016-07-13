# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/5/524.pdf
0<n<=16, the max sum is 31 (16+15)
"""

import sys
from collections import deque
from io import StringIO
from multiprocessing.pool import Pool

sieves = (0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
          1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0)

ans = [
    [],  # 0
    [[1], ],  # 1
    [[1, 2], ],  # 2
    [],
    [[1, 2, 3, 4], [1, 4, 3, 2]],
    [],
    [[1, 4, 3, 2, 5, 6], [1, 6, 5, 2, 3, 4]],
    [],
    [[1, 2, 3, 8, 5, 6, 7, 4], [1, 2, 5, 8, 3, 4, 7, 6],
     [1, 4, 7, 6, 5, 8, 3, 2], [1, 6, 7, 4, 3, 8, 5, 2]],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]


def solve(n):
    # (pos, chosen, ring)
    stack = deque([(1, [True] + [False] * (n - 1), [1, ])])
    stack_pop = stack.popleft
    stack_append = stack.append
    sio = StringIO()
    while stack:
        pos, chosen, ring = stack_pop()
        if pos == n:
            if sieves[ring[pos - 1] + ring[0]]:
                sio.write("{}\n".format(" ".join(map(str, ring))))
                # print (" ".join(map(str, ring)))
                # print("[{}],".format(",".join(map(str, ring))))
            continue
        for idx in range(n):
            if not chosen[idx] and sieves[ring[-1] + (idx + 1)]:
                chosen[idx] = True
                stack_append([pos + 1, chosen[:], ring + [idx + 1]])
                chosen[idx] = False

    return sio.getvalue()


def main():
    recs = sys.stdin.readlines()

    pool = Pool(6)
    ans = pool.map(solve, range(1, 17))

    for tdx, rec in enumerate(recs):
        n = int(rec)

        if tdx:
            print()

        print("Case {}:".format(tdx + 1))
        # pre-computing
        if n in (3, 5, 7, 9, 11, 13, 15):
            continue
        else:
            print(ans[n - 1], end="")


if __name__ == '__main__':
    main()
