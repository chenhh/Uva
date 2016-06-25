# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/469.pdf
"""

import sys


def dfs(maze, x0, y0):
    n_row, n_col = len(maze), len(maze[0])
    # N, E, S, W, NE, NS
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    stack = [(x0, y0)]
    visited = [[False] * n_col for _ in range(n_row)]
    visited[x0][y0] = True
    n_lake = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            x1, y1 = x + dx, y + dy
            if (0 <= x1 < n_row and 0 <= y1 < n_col and maze[x1][y1] == 'W' and
                        visited[x1][y1] is False):
                stack.append((x1, y1))
                visited[x1][y1] = True
                n_lake += 1

    return n_lake


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        try:
            maze, querys = [], []
            while True:
                data = next(recs).strip()
                if data:
                    if data[0] in ('L', 'W'):
                        maze.append(data)
                    else:
                        querys.append(tuple(map(int, data.split())))
                else:
                    raise GeneratorExit

        except (StopIteration, GeneratorExit):
            # print (maze)
            for px, py in querys:
                x, y = px - 1, py - 1
                if maze[x][y] == 'L':
                    print(0)
                else:
                    n_lake = dfs(maze, x, y)
                    print(n_lake)
            if tdx != n_case - 1:
                print()


if __name__ == '__main__':
    main()
