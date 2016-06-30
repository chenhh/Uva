# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/106/10685.pdf
the same as 11503
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        while True:
            data = next(recs).strip()
            if data:
                n_node, n_edge = list(map(int, data.split()))
                break
        if not n_node and not n_edge:
            break

        roots = {}
        for _ in range(n_node):
            k = next(recs).strip()
            roots[k] = k

        groups = {k: set([k]) for k in roots.keys()}
        for _ in range(n_edge):
            n1, n2 = next(recs).split()

            if roots[n1] != roots[n2]:
                # n1, n2 in different sets.
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

        print(max(len(s) for s in groups.values()))


if __name__ == '__main__':
    main()
