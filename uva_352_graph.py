# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/3/352.pdf
"""

import sys


def dfs(image, rdx, cdx, dim):
    """
    the image is call by reference
    mark all connected compoents to zero.
    """
    # N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    stack = [(rdx, cdx)]
    while stack:
        x, y = stack.pop()
        if image[x][y] == '1':
            image[x][y] = '0'
            for h, v in directions:
                if 0 <= x + h < dim and 0 <= y + v < dim:
                    stack.append((x + h, y + v))


def main():
    recs = iter(sys.stdin.readlines())

    case = 0
    while 1:
        try:
            dim = int(next(recs))
            image = [list(next(recs).strip()) for _ in range(dim)]
            n_eagle = 0
            for rdx in range(dim):
                for cdx in range(dim):
                    if image[rdx][cdx] == '1':
                        # the image is passed by reference
                        dfs(image, rdx, cdx, dim)
                        n_eagle += 1
            case += 1
            print("Image number {} contains {} war eagles.".format(
                case, n_eagle))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
