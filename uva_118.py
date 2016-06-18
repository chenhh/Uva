# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/118.pdf
http://luckycat.kshs.kh.edu.tw/homework/q118.htm
"""

import sys


def main():
    angles = {'E': 0, 'N': 90, 'W': 180, 'S': 270}
    directions = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}

    recs = iter(sys.stdin.readlines())
    # the upper-right coordinates
    map_x, map_y = list(map(int, next(recs).split()))
    scents = set()
    while 1:
        try:
            locs = next(recs).split()
            cmds = next(recs).strip()

            # initial location and direction
            x, y, angle = int(locs[0]), int(locs[1]), angles[locs[2]]
            lost = False
            for cmd in cmds:
                next_x, next_y = x, y
                if cmd == 'L':
                    angle = (angle + 90) % 360
                elif cmd == 'R':
                    angle = (angle - 90) % 360
                elif cmd == 'F':
                    if angle == 0:
                        next_x += 1
                    elif angle == 90:
                        next_y += 1
                    elif angle == 180:
                        next_x -= 1
                    elif angle == 270:
                        next_y -= 1
                # the current cmd will make robot fall out map
                if (next_x < 0 or next_x > map_x or
                            next_y < 0 or next_y > map_y):
                    # ignore the falling command which was shown before
                    if (x, y) not in scents:
                        lost = True
                        scents.add((x, y))
                        break
                else:
                    x, y = next_x, next_y

            msgs = (str(x), str(y), directions[angle], "LOST" if lost else "")
            print(" ".join(msgs).strip())

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
