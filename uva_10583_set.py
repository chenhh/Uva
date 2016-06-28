# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/105/10583.pdf
using dfs will TLE, using set union
"""

import sys


def components(graph, n_node):
    """
    graph: edge list
    TLE
    """
    start = 0
    stack = [start, ]
    visited = [-1] * n_node
    com_id = 1
    visited[start] = com_id
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if visited[child] == -1:
                stack.append(child)
                visited[child] = com_id
        # print (visited)
        if not stack:
            com_id += 1
            for idx, v in enumerate(visited):
                if v == -1:
                    stack.append(idx)
                    visited[idx] = com_id
                    break
    return max(visited)


def TLE_main():
    recs = iter(sys.stdin.readlines())

    case = 0
    while True:
        n_node, n_edge = list(map(int, next(recs).split()))
        if not n_node:
            break
        # undirected graph
        graph = [[] for _ in range(n_node)]
        for _ in range(n_edge):
            n1, n2 = list(map(int, next(recs).split()))
            graph[n1 - 1].append(n2 - 1)
            graph[n2 - 1].append(n1 - 1)

        case += 1
        # print (graph)
        ans = components(graph, n_node)
        print("Case {}: {}".format(case, ans))


def main():
    recs = iter(sys.stdin.readlines())

    case = 0
    while True:
        n_node, n_edge = list(map(int, next(recs).split()))
        if not n_node:
            break
        # undirected graph
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

        ans = sum(1 for g in groups if g)
        case += 1
        print("Case {}: {}".format(case, ans))


if __name__ == '__main__':
    main()
