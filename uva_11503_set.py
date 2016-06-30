# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11503.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        n_link = int(next(recs))

        roots, groups = {}, {}
        for _ in range(n_link):
            n1, n2 = next(recs).split()
            nodes = roots.keys()

            if n1 not in nodes and n2 not in nodes:
                # both names are not in any sets
                # n1 may be the same as n2
                roots[n1] = n1
                roots[n2] = n1
                groups[roots[n1]] = set([n1, n2])
            elif n1 in nodes and n2 not in nodes:
                # union n2 to n1
                # n1 may be the same as n2
                roots[n2] = roots[n1]
                groups[roots[n1]].add(n2)
            elif n1 not in nodes and n2 in nodes:
                # union n1 to n2
                # n1 may be the same as n2
                roots[n1] = roots[n2]
                groups[roots[n2]].add(n1)
            elif n1 in nodes and n2 in nodes and roots[n1] != roots[n2]:
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
            # print (n1, n2)
            # print(roots)
            # print (groups)
            print(len(groups[roots[n2]]))


if __name__ == '__main__':
    main()
