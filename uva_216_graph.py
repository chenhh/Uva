# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/216.pdf
the problem requires linear structure, we can't not using greedy method because
local optimal may not be the global optimal, solved by listed all permutations.
"""

import math
import sys
from itertools import permutations


def main():
    recs = iter(sys.stdin.readlines())
    lsqrt = math.sqrt

    case = 0
    while 1:
        n_node = int(next(recs))
        if not n_node:
            break
        nodes = [list(map(int, (next(recs).split()))) for _ in range(n_node)]
        graph = [[0] * n_node for _ in range(n_node)]
        for idx in range(n_node - 1):
            for jdx in range(idx + 1, n_node):
                graph[idx][jdx] = graph[jdx][idx] = (
                    lsqrt((nodes[idx][0] - nodes[jdx][0]) *
                          (nodes[idx][0] - nodes[jdx][0]) +
                          (nodes[idx][1] - nodes[jdx][1]) *
                          (nodes[idx][1] - nodes[jdx][1])))

        min_perm, min_dist = None, 2 << 31
        for perm in permutations(range(n_node)):
            dist = sum(graph[min(perm[kdx], perm[kdx + 1])]
                       [max(perm[kdx], perm[kdx + 1])]
                       for kdx in range(n_node - 1))
            if dist < min_dist:
                min_dist = dist
                min_perm = perm

        case += 1
        print('**********************************************************')
        print("Network #{}".format(case))
        for idx in range(1, n_node):
            sdx, edx = min_perm[idx - 1], min_perm[idx]
            x1, y1 = nodes[sdx]
            x2, y2 = nodes[edx]
            print("Cable requirement to connect ({},{}) to ({},{}) is {:.2f} "
                  "feet.".format(x1, y1, x2, y2, graph[sdx][edx] + 16))
        print("Number of feet of cable required is {:.2f}.".format(
            min_dist + (n_node - 1) * 16))


if __name__ == '__main__':
    main()
