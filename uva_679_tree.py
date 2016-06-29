# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/6/679.pdf
http://luckycat.kshs.kh.edu.tw/homework/q679.htm

full binary tree, using list to implement FBT.
(the root node is located in index 1)
assuming that the current node in index t, then
the left child is located in index 2*t, and
the right child is located in index 2*t+1
"""

import sys


def TLE_main():
    """ direct simulation correct but TLE """
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        depth, n_ball = list(map(int, next(recs).split()))
        size = (2 ** depth)
        last_internal_nodes = 2 ** (depth - 1) - 1

        tree = [False] * size
        for ball in range(1, n_ball + 1):
            pos = 1
            while pos <= last_internal_nodes:
                if tree[pos]:
                    # go right while true
                    tree[pos] = False
                    pos = pos + pos + 1
                else:
                    # go left while false
                    tree[pos] = True
                    pos = pos + pos
        print(pos)


def main():
    """
    The path from root (rightmost) to leaf (leftmost) of FBT is a binary number
    with D digits, and the leftmost bit must be 1.

    e.g. D=4, then the binary must be 1xxx (x may be 0 or 1).
    1st: 1000 (in position 8) 000 = 0
    2nd: 1100 (in position 12) 001 = 1
    3rd: 1010 (in position 10) 010 = 2
    4th: 1110 (in position 14) 011 = 3
    """

    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        depth, n_ball = list(map(int, next(recs).split()))
        binary = 1 << (depth - 1)

        n_ball -= 1
        for jdx in reversed(range(depth - 1)):
            binary |= (n_ball % 2) << jdx
            n_ball //= 2

        print(binary)


if __name__ == '__main__':
    main()
