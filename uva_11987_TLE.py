# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/119/11987.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11987.htm

1, p ,q: Union the sets containing p and q.
    If p and q are already in the same set, ignore this command.
2, p, q: Move p to the set containing q.
    If p and q are already in the same set, ignore this command.
3, p: Return the number of elements and the sum of elements in the set
    containing p.

"""
import sys

def main():
    """  correct, but TLE """

    while 1:
        try:
            n_value, n_cmd = list(map(int, input().split()))
            # list record the value in which set
            roots = list(range(n_value))
            collections = [[v] for v in range(n_value)]

            for _ in range(n_cmd):
                vals = list(map(int, input().split()))
                if len(vals) == 3:
                    t, p, q = vals
                    root_p, root_q = roots[p - 1], roots[q - 1]
                    if root_p == root_q:
                        continue

                    if t == 1:
                        # union, maintain the set with larger set
                        if len(collections[root_p]) > len(collections[root_q]):
                            set_src, set_tgt = root_q, root_p
                        else:
                            set_src, set_tgt = root_p, root_q

                        # elements in source set
                        for src in collections[set_src]:
                            roots[src] = set_tgt
                            collections[set_tgt].append(src)
                        collections[set_src].clear()

                    elif t == 2:
                        # move p to the set containing of q
                        collections[roots[p - 1]].remove(p - 1)
                        collections[roots[q - 1]].append(p - 1)
                        roots[p - 1] = roots[q - 1]

                elif len(vals) == 2:
                    # t == 3
                    t, p = vals
                    root_p = roots[p - 1]
                    set_p_all = collections[root_p]
                    print(len(set_p_all), sum(set_p_all) + len(set_p_all))

                print (vals)
                print (roots)
                print (collections)

        except (EOFError):
            break


if __name__ == '__main__':
    main()
