# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/459.pdf
http://luckycat.kshs.kh.edu.tw/homework/q459.htm
"""

import sys


def connected_components(graph, n_node):
    if n_node == 0:
        return 0
    stack = [0, ]
    visited = [False] * n_node

    n_sub = 1
    while not all(visited):
        # print ("Stack:", stack)
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    stack.append(child)
        if not stack:
            for idx, val in enumerate(visited):
                if not val:
                    stack.append(idx)
                    n_sub += 1
                    break
    return n_sub


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        node = next(recs).strip()
        graph = [[] for _ in range(ord(node) - ord('A') + 1)]
        try:
            while 1:
                line = next(recs).strip()
                if not line:
                    raise GeneratorExit
                edge = list(map(lambda x: ord(x) - ord('A'), line))
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

        except (StopIteration, GeneratorExit):
            if tdx:
                print()
            print(connected_components(graph, len(graph)))


if __name__ == '__main__':
    main()
