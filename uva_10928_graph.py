# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10928.pdf
output the node with minimum degree
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        while True:
            data = next(recs).strip()
            if data:
                n_node = int(data)
                break
        graph = [len(next(recs).split()) for _ in range(n_node)]
        min_degree = min(graph)
        ans = [str(ndx + 1) for ndx, degree in enumerate(graph)
               if degree == min_degree]
        print(" ".join(ans))


if __name__ == '__main__':
    main()
