# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/7/784.pdf
"""

import sys

# N, NE, E, SE, S, SW, W, NW
directions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
              (-1, -1))


def maze_walking(maze):
    """ the maze is an irregular shape image and containing last line"""
    # find start point
    n_row = len(maze) - 1
    pt = None

    for rdx, row in enumerate(maze):
        if pt:
            break
        for cdx, v in enumerate(row):
            if v == '*':
                pt = (rdx, cdx)

    stack = [pt, ]
    maze[pt[0]][pt[1]] = ' '
    while stack:
        x, y = stack.pop()
        if maze[x][y] == ' ':
            maze[x][y] = '#'
            for h, v in directions:
                if (0 <= x + h < n_row and 0 <= y + v < len(maze[x + h]) and
                            maze[x + h][y + v] == ' '):
                    stack.append((x + h, y + v))

    # print maze
    for row in maze:
        print(''.join(row))


def main():
    recs = iter(sys.stdin.readlines())
    n_maze = int(next(recs))
    maze = []
    for _ in range(n_maze):
        maze.clear()
        while 1:
            line = next(recs).strip()
            maze.append(list(line))
            if line[0] == '_':
                break
        maze_walking(maze)


if __name__ == '__main__':
    main()
