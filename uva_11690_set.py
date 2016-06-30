# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/116/11690.pdf

POSSIBLE if all the sum of the nodes in the same sets are zeros.
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        n_node, n_edge = list(map(int, next(recs).split()))

        moneys = [int(next(recs)) for _ in range(n_node)]
        roots = [v for v in range(n_node)]
        groups = {v: set([v]) for v in range(n_node)}

        for _ in range(n_edge):
            n1, n2 = list(map(int, next(recs).split()))
            if roots[n1] != roots[n2]:
                # n1, n2 in different sets, union
                s1, s2 = len(groups[roots[n1]]), len(groups[roots[n2]])
                if s1 < s2:
                    # merge s1 to s2
                    tmp = roots[n1]
                    for node in groups[tmp]:
                        roots[node] = roots[n2]
                        groups[roots[n2]].add(node)
                    del groups[tmp]
                else:
                    # merge s2 to s1
                    tmp = roots[n2]
                    for node in groups[tmp]:
                        roots[node] = roots[n1]
                        groups[roots[n1]].add(node)
                    del groups[tmp]
        possible = True
        for group in groups.values():
            remain = sum(moneys[v] for v in group)
            if remain != 0:
                possible = False
                break
        print("POSSIBLE" if possible else "IMPOSSIBLE")


if __name__ == '__main__':
    main()
