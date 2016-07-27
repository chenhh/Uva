# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

869 Airline Comparison

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/8/869.pdf
"""

import sys
from collections import deque


def is_equal(graph1, graph2):
    nodes = graph1.keys()
    if nodes != graph2.keys():
        return "NO"

    nodes = list(nodes)
    visited = {k: 0 for k in nodes}

    stack = deque([nodes[0]])
    visited[nodes[0]] = 1
    while stack:
        curr = stack.pop()
        for child in graph1[curr]:
            if not visited[child]:
                visited[child] = visited[curr]
                stack.append(child)

        if not stack:
            for k, v in visited.items():
                if not v:
                    visited[k] = visited[curr] + 1
                    stack.append(k)

    visited2 = {k: 0 for k in nodes}
    stack.append(nodes[0])
    visited2[nodes[0]] = 1
    while stack:
        curr = stack.pop()
        for child in graph2[curr]:
            if not visited2[child]:
                visited2[child] = visited2[curr]
                stack.append(child)

        if not stack:
            for k, v in visited2.items():
                if not v:
                    visited2[k] = visited2[curr] + 1
                    stack.append(k)

    return "YES" if visited == visited2 else "NO"


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        while True:
            data = next(recs).strip()
            if data:
                n_flight1 = int(data)
                break
        graph1 = {}
        for _ in range(n_flight1):
            src, tgt = next(recs).split()
            graph1.setdefault(src, []).append(tgt)
            graph1.setdefault(tgt, []).append(src)

        n_flight2 = int(next(recs))
        graph2 = {}

        for _ in range(n_flight2):
            src, tgt = next(recs).split()
            graph2.setdefault(src, []).append(tgt)
            graph2.setdefault(tgt, []).append(src)

        if tdx:
            print()
        print(is_equal(graph1, graph2))


if __name__ == '__main__':
    main()
