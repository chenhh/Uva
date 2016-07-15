# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/439.pdf
http://luckycat.kshs.kh.edu.tw/homework/q439.htm

https://en.wikipedia.org/wiki/Knight_(chess)
BFS search
"""

import sys
from collections import deque


def main():
    row_dict = {chr(ord('a') + v): v for v in range(9)}
    moves = ((2, 1), (2, -1), (1, 2), (1, -2),
             (-1, 2), (-1, -2), (-2, 1), (-2, -1))

    recs = iter(sys.stdin.readlines())

    stack = deque()
    stack_append = stack.append
    stack_pop = stack.popleft
    stack_clear = stack.clear
    for rec in recs:
        # the boundary is from 0 to 7.
        src, tgt = rec.split()
        step = 0
        if src != tgt:
            visited = [[False] * 8 for _ in range(8)]
            stack_clear()
            x0, y0 = row_dict[src[0]], int(src[1]) - 1
            xt, yt = row_dict[tgt[0]], int(tgt[1]) - 1
            # (x, y, step)
            stack_append((x0, y0, 0))
            visited[x0][y0] = True

            # BFS search
            while stack:
                x, y, depth = stack_pop()
                if x == xt and y == yt:
                    step = depth
                    break

                for dx, dy in moves:
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < 8 and 0 <= y1 < 8 and not visited[x1][y1]:
                        stack_append((x1, y1, depth + 1))
                        visited[x1][y1] = True

        print("To get from {} to {} takes {} knight moves.".format(
            src, tgt, step))


if __name__ == '__main__':
    main()
