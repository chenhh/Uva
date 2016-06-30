# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/11/1197.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        n_node, n_group = list(map(int, next(recs).split()))
        if not n_node:
            break

        roots = [v for v in range(n_node)]
        groups = {v: set([v]) for v in range(n_node)}
        for _ in range(n_group):
            vals = list(map(int, next(recs).split()))
            n_member, nodes = vals[0], vals[1:]

            for idx in range(1, n_member):
                n1, n2 = nodes[idx - 1], nodes[idx]
                if roots[n1] != roots[n2]:
                    # n1, n2 in different sets, union
                    s1, s2 = len(groups[roots[n1]]), len(groups[roots[n2]])
                    if s1 < s2:
                        # merge s1 to s2
                        tmp = roots[n1]
                        for node in groups[tmp]:
                            roots[node] = roots[n2]
                            groups[roots[n2]].add(node)
                        groups[tmp].clear()
                    else:
                        # merge s2 to s1
                        tmp = roots[n2]
                        for node in groups[tmp]:
                            roots[node] = roots[n1]
                            groups[roots[n1]].add(node)
                        groups[tmp].clear()
        # print (groups)
        print(len(groups[roots[0]]))


if __name__ == '__main__':
    main()
