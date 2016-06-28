# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/7/793.pdf
online connected components
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        try:
            while True:
                data = next(recs).strip()
                if data:
                    n_node = int(data)
                    break

            # record the group idx of each node
            roots = [v for v in range(n_node)]
            # record the nodes in the group
            groups = [set([v]) for v in range(n_node)]
            success, not_success = 0, 0
            while True:
                data = next(recs).strip()
                if not data:
                    raise GeneratorExit
                form, n1, n2 = data.split()
                n1, n2 = int(n1) - 1, int(n2) - 1
                if form == 'c':
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
                elif form == 'q':
                    if roots[n1] == roots[n2]:
                        # in the same set
                        success += 1
                    else:
                        # in different set
                        not_success += 1

        except (GeneratorExit, StopIteration):
            print("{},{}".format(success, not_success))
            if tdx != n_case - 1:
                print()


if __name__ == '__main__':
    main()
