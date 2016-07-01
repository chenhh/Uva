# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 2

https://uva.onlinejudge.org/external/101/10158.pdf

c = 1, setFriends
c = 2, setEnemies
c = 3, areFriends
c = 4, areEnemies
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_node = int(next(recs))

    roots = [v for v in range(n_node)]
    groups = {v: set([v]) for v in range(n_node)}

    while True:
        try:
            cmd, n1, n2 = list(map(int, (next(recs)).split()))
            if not cmd:
                break

            ans = None
            if cmd in (1, 2):
                # set friend or emeny
                if -n1 in groups[roots[n2]] or -n2 in groups[roots[n1]]:
                    ans = -1
                elif roots[n1] != roots[n2]:
                    s1, s2 = len(groups[roots[n1]]), len(groups[roots[n2]])
                    if s1 < s2:
                        # merge s1 to s2
                        tmp = roots[n1]
                        for node in groups[tmp]:
                            roots[abs(node)] = roots[n2]
                            groups[roots[n2]].add(node)
                        del groups[tmp]
                    else:
                        # merge s2 to s1
                        tmp = roots[n2]
                        for node in groups[tmp]:
                            roots[abs(node)] = roots[n1]
                            groups[roots[n1]].add(node)
                        del groups[tmp]
            elif cmd == 3:
                # are x and y in the same set?
                ans = 1 if roots[n1] == roots[n2] else 0

            elif cmd == 4:
                # are x and y in different sets?
                if roots[n1] == roots[n2]:
                    if -n1 in groups[roots[n1]] or -n2 in groups[roots[n1]]:
                        ans = 1
                else:
                    ans = 0
            print(ans)

        except (GeneratorExit, StopIteration):
            break


if __name__ == '__main__':
    main()
