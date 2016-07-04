# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/785.pdf

the boundary character is 'X' and there is no char outside the 'X'.
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    maze = []
    maze_append = maze.append
    maze_clear = maze.clear

    visited = []
    visited_append = visited.append
    visited_clear = visited.clear
    stack = []
    stack_pop = stack.pop
    stack_append = stack.append
    stack_clear = stack.clear

    while True:
        try:
            data = next(recs).strip('\n')
            if data and data[0] == '_':

                n_row = len(maze)
                curr_rdx = 0
                draw_char = None
                stack_clear()

                # find all start
                for rdx, row in enumerate(maze):
                    for cdx, c in enumerate(row):
                        if c != 'X' and c != ' ':
                            stack_append((rdx, cdx, c))
                            visited[rdx][cdx] = True

                while stack:
                    x, y, c = stack_pop()
                    for dx, dy in directions:
                        x1, y1 = x + dx, y + dy
                        if (0 <= x1 < n_row and 0 <= y1 < len(maze[x1]) and
                                    maze[x1][y1] != 'X' and
                                not visited[x1][y1]):
                            stack_append((x1, y1, c))
                            visited[x1][y1] = True
                            maze[x1][y1] = c

                for row in maze:
                    print("".join(row))
                print(data)

                # reset
                maze_clear()
                visited_clear()
            else:
                maze_append(list(data))
                visited_append([False] * len(data))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
