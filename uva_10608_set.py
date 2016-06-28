# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/106/10608.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for _ in range(n_case):
        n_node, n_edge = list(map(int, next(recs).split()))
        if n_edge == 0:
            # no any friend
            print(0)
            continue

        roots = [v for v in range(n_node)]
        groups = [set([v]) for v in range(n_node)]
        for _ in range(n_edge):
            v1, v2 = list(map(int, next(recs).split()))
            n1, n2 = v1 - 1, v2 - 1

            if roots[n1] != roots[n2]:
                # union, merge small group to large one
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

        ans = max(len(g) for g in groups)
        print(ans)


if __name__ == '__main__':
    main()
