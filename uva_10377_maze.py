# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10377.pdf
"""

import sys

states = {
    'N': (-1, 0),  # north
    'E': (0, 1),  # east
    'S': (1, 0),  # south
    'W': (0, -1),  # west
}

directions = 'NESW'


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        try:
            n_row, n_col = list(map(int, next(recs).split()))
            maze = [next(recs) for _ in range(n_row)]
            # initial position, always face north
            x0, y0 = list(map(int, next(recs).split()))

            cmds = []
            while True:
                data = next(recs).split()
                if not data:
                    raise GeneratorExit
                cmds.extend(data)

        except (GeneratorExit, StopIteration):
            x, y = x0 - 1, y0 - 1
            direction = 0
            state = states[directions[direction]]

            cmds = "".join(cmds)
            for cmd in cmds:
                # print ('{} {} {}'.format(x, y, directions[direction]))
                if cmd == 'R':
                    # turn right
                    direction = (direction + 1) % 4
                    state = states[directions[direction]]
                elif cmd == 'L':
                    # turn left
                    direction = (direction - 1) % 4
                    state = states[directions[direction]]
                elif cmd == 'F':
                    # move forward
                    x1, y1 = x + state[0], y + state[1]
                    if (0 <= x1 < n_row and 0 <= y1 < n_col and
                                maze[x1][y1] == ' '):
                        x, y = x1, y1
                elif cmd == 'Q':
                    print("{} {} {}".format(
                        x + 1, y + 1, directions[direction]))
                    if tdx != n_case - 1:
                        print()


if __name__ == '__main__':
    main()
