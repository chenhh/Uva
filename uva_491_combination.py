# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

491 - Tile Topology

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/491.pdf

http://mathworld.wolfram.com/Polyomino.html
"""

import sys


def main():
    n_shapes = [0, 1, 1, 2, 7, 18, 60, 196, 704, 2500, 9189, 33896, 126759,
                476270, 1802312, 6849777]

    recs = sys.stdin.readlines()
    for rec in recs:
        print(n_shapes[int(rec)])


if __name__ == '__main__':
    main()
