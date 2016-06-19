# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/100/10034.pdf
minimum spanning tree
"""

import math
import sys


def mst(locs, n_node):
    """
    uva 10034
    full connected graph, and the locs are the coordinates the each node.
    Kruskal's algorithm
    """
    lsqrt = math.sqrt
    graph = {}
    for idx in range(n_node):
        x1, y1 = locs[idx]
        for jdx in range(idx + 1, n_node):
            x2, y2 = locs[jdx]
            dx, dy = (x1 - x2), (y1 - y2)
            graph[(idx, jdx)] = lsqrt(dx * dx + dy * dy)
    graph = sorted(graph.items(), key=lambda x: x[1])

    # store the id in which set
    sets = list(range(n_node))
    # store the set contains what ids
    groups = [[idx] for idx in range(n_node)]
    n_edge, costs = 0, 0
    for gdx, ((n1, n2), d) in enumerate(graph):
        if sets[n1] != sets[n2]:
            costs += d
            n_edge += 1
            # union set, merge small set to large one
            if len(groups[sets[n1]]) > len(groups[sets[n2]]):
                groups[sets[n1]].extend(groups[sets[n2]])
                tmp = sets[n2]
                for idx in groups[sets[n2]]:
                    sets[idx] = sets[n1]
                groups[tmp].clear()

            else:
                groups[sets[n2]].extend(groups[sets[n1]])
                tmp = sets[n1]
                for idx in groups[sets[n1]]:
                    sets[idx] = sets[n2]
                groups[tmp].clear()

        if n_edge == n_node - 1:
            break

    return costs


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)
    locs = []
    append = locs.append
    for tdx in range(n_case):
        try:
            n_node = int(next(recs))
            locs.clear()
            while 1:
                data = next(recs).strip()
                if not data:
                    break
                append(list(map(float, data.split())))
            if tdx:
                print()
            print("{:.2f}".format(mst(locs, n_node)))

        except (StopIteration):
            if locs:
                if tdx:
                    print()
                print("{:.2f}".format(mst(locs, n_node)))
            break


if __name__ == '__main__':
    main()
