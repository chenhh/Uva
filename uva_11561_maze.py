# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11561.pdf
"""

import sys
from collections import deque
from itertools import product


def main():
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    recs = iter(sys.stdin.readlines())
    stack = deque()
    stack_clear = stack.clear
    stack_append = stack.append
    stack_pop = stack.pop

    while True:
        try:
            n_col, n_row = list(map(int, next(recs).split()))
            maze = [list(next(recs).strip()) for _ in range(n_row)]
            visited = [[0] * n_col for _ in range(n_row)]
            coordinates = product(range(n_row), range(n_col))

            stack_clear()
            for x, y in coordinates:
                c = maze[x][y]
                if c == 'P':
                    # initial position
                    stack_append((x, y))
                elif c == 'T':
                    # stop regions
                    for dx, dy in directions:
                        x1 = x + dx
                        y1 = y + dy
                        if (0 <= x1 < n_row and 0 <= y1 < n_col and
                                not visited[x1][y1]):
                            visited[x1][y1] = -1

            # the initial position is nearby a trap
            if visited[stack[0][0]][stack[0][1]] == -1:
                print(0)
                continue

            # DFS
            n_gold = 0
            while stack:
                x, y = stack_pop()
                # print (x, y)
                for dx, dy in directions:
                    x1 = x + dx
                    y1 = y + dy
                    if (0 <= x1 < n_row and 0 <= y1 < n_col and
                                maze[x1][y1] != '#'):
                        if not visited[x1][y1]:
                            # not a visited or stop region, move forward
                            stack_append((x1, y1))

                        if visited[x1][y1] != 1 and maze[x1][y1] == 'G':
                            # not a visited region
                            n_gold += 1

                        visited[x1][y1] = 1
            print(n_gold)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
