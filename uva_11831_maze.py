# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/118/11831.pdf
"""

import sys

states = {
    'N': (-1, 0),  # north
    'L': (0, 1),  # east
    'S': (1, 0),  # south
    'O': (0, -1),  # west
}


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        n_row, n_col, n_cmd = list(map(int, next(recs).split()))
        if not n_row:
            break
        maze = [list(next(recs).strip()) for _ in range(n_row)]
        cmds = []
        while True:
            cmds.extend(list(next(recs).strip()))
            if len(cmds) >= n_cmd:
                break
        # find initial position
        state = (None, None)
        x, y = None, None
        for idx in range(n_row):
            if x and y:
                break
            for jdx in range(n_col):
                if maze[idx][jdx] in ('N', 'S', 'L', 'O'):
                    x, y = idx, jdx
                    state = states[maze[idx][jdx]]

        n_sticker = 0
        for cmd in cmds:
            # print('cmd:', cmd, "position:", x, y, 'state:', state)
            if cmd == 'F':
                # move forward
                x1, y1 = x + state[0], y + state[1]
                # not a pillar and still in the arena
                if 0 <= x1 < n_row and 0 <= y1 < n_col and maze[x1][y1] != '#':
                    x, y = x1, y1
                    if maze[x][y] == '*':
                        n_sticker += 1
                        maze[x][y] = '.'
            elif cmd == 'D':
                # turn right
                if state == states['N']:
                    # north to east
                    state = states['L']
                elif state == states['L']:
                    # east to south
                    state = states['S']
                elif state == states['S']:
                    # south to west
                    state = states['O']
                elif state == states['O']:
                    # west to north
                    state = states['N']
            elif cmd == 'E':
                # turn left
                if state == states['N']:
                    # north to west
                    state = states['O']
                elif state == states['O']:
                    # west to south
                    state = states['S']
                elif state == states['S']:
                    # south to east
                    state = states['L']
                elif state == states['L']:
                    # east to north
                    state = states['N']

        print(n_sticker)


if __name__ == '__main__':
    main()
