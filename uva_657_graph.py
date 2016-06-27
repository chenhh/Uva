# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/6/657.pdf

e.g.
10 2
..X**X***X
..XXXX....
0 0

ans: 2

2 2
..
..
0 0
ans: 0
"""

import sys
from copy import copy

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))


def components(image):
    """
    computer the disconnected number of X in disconnected region *
    two-stage
     # .: background, *: a die, 'X: a die's dot
    """
    n_row, n_col = len(image), len(image[0])
    global directions

    stack = []
    x_pos = set()
    x_components = []

    # find all components
    for idx in range(n_row):
        if stack:
            break
        for jdx in range(n_col):
            if image[idx][jdx] in ('*', 'X'):
                stack.append((idx, jdx))
                if image[idx][jdx] == 'X':
                    x_pos.add((idx, jdx))
                image[idx][jdx] = '.'
                break

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            x1, y1 = x + dx, y + dy
            if (0 <= x1 < n_row and 0 <= y1 < n_col and
                        image[x1][y1] in ('*', 'X')):
                if image[x1][y1] == 'X':
                    x_pos.add((x1, y1))
                stack.append((x1, y1))
                image[x1][y1] = '.'

        # find next components
        if not stack:
            x_components.append(copy(x_pos))
            x_pos.clear()

            # find initial position
            for idx in range(n_row):
                if stack:
                    break
                for jdx in range(n_col):
                    if image[idx][jdx] in ('*', 'X'):
                        if image[idx][jdx] == 'X':
                            x_pos.add((idx, jdx))
                        stack.append((idx, jdx))
                        image[idx][jdx] = '.'
                        break

    # traversal X components
    if not len(x_components):
        return 0

    dots = [0] * len(x_components)
    for idx, pos in enumerate(x_components):
        x0, y0 = pos.pop()
        stack = [(x0, y0)]
        n_dot = 1
        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < n_row and 0 <= y1 < n_col and (x1, y1) in pos:
                    stack.append((x1, y1))
                    pos.remove((x1, y1))

            if not stack and pos:
                n_dot += 1
                x0, y0 = pos.pop()
                stack.append((x0, y0))

        dots[idx] = n_dot

    dots.sort()
    return " ".join(str(v) for v in dots)


def main():
    recs = iter(sys.stdin.readlines())
    case = 0
    while True:
        width, height = list(map(int, next(recs).split()))
        if not width:
            break
        # .: background, *: a die, 'X: a die's dot
        # Dice may have different sizes and not be entirely square
        # due to optical distortion
        image = [list(next(recs).strip()) for _ in range(height)]
        case += 1
        print("Throw {}".format(case))
        print(components(image))
        print()


if __name__ == '__main__':
    main()
