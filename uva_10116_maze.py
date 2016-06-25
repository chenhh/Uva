# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/101/10116.pdf
"""

import sys

move = {'N': (-1, 0), 'E': (0, 1), 'W': (0, -1), 'S': (1, 0)}


def walk(maze, n_row, n_col, start_col):
    """
    the direction in the maze may form a loop
    if a position is visited twice, then it will form a loop.
    position (x,y): x*n_col + y
    """
    n_pos = n_row * n_col
    visited =[False]*(n_pos)
    seqs = []
    x, y = 0, start_col - 1

    for _ in range(n_pos+1):
        pos = x*n_col+y
        if visited[pos]:
            # loop, and find loop start idx
            loop_sdx = seqs.index(pos)
            n_step, n_loop = loop_sdx, len(seqs) - loop_sdx
            return "{} step(s) before a loop of {} step(s)".format(
                n_step, n_loop)

        visited[pos] = True
        seqs.append(pos)
        dx, dy = move[maze[x][y]]
        x1, y1 = x+dx, y+dy
        if 0 <= x1 < n_row and 0<=y1< n_col:
            x, y = x1, y1
        else:
            # normal exit
            n_step = len(seqs)
            return "{} step(s) to exit".format(n_step)


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        n_row, n_col, start_col = list(map(int, next(recs).split()))
        if not n_row:
            break

        maze = [next(recs).strip() for _ in range(n_row)]
        print (walk(maze, n_row, n_col, start_col))

if __name__ == '__main__':
    main()