# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/3/336.pdf
http://luckycat.kshs.kh.edu.tw/homework/q336.htm
BFS
"""

import sys
from collections import deque


def BFS(graph, n_node, start, ttl):
    """ the graph is a dict of list """
    visited = {k: False for k in graph.keys()}
    depth = {k: -1 for k in graph.keys()}
    parents = {k: -1 for k in graph.keys()}
    # (parent, node)
    queue = deque([(start, start), ])

    while queue:
        parent, node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            parents[node] = parent
            if depth[parent] >= ttl:
                break
            depth[node] = depth[parent] + 1

            for child in graph[node]:
                if not visited[child]:
                    queue.append((node, child))

    return (sum(1 for _, v in depth.items() if v == -1))


def main():
    recs = iter(sys.stdin.readlines())
    query_num = 0

    while True:
        data = next(recs).strip()
        if data:
            n_edge = int(data)
            if n_edge == 0:
                break
        else:
            continue

        # edges
        edges = []
        while True:
            edges.extend(list(map(int, next(recs).split())))
            if len(edges) >= n_edge * 2:
                break

        graph = {}
        for idx in range(n_edge):
            n1, n2 = idx * 2, idx * 2 + 1
            graph.setdefault(edges[n1], []).append(edges[n2])
            graph.setdefault(edges[n2], []).append(edges[n1])

        # questions
        querys = []
        while True:
            values = list(map(int, next(recs).split()))
            if values[-1] == 0 and values[-2] == 0:
                querys.extend(values[:-2])
                break
            querys.extend(values)

        n_query = len(querys) // 2
        node_ids = graph.keys()
        for jdx in range(n_query):
            start, ttl = querys[jdx * 2], querys[jdx * 2 + 1]
            query_num += 1
            if start not in node_ids:
                ans = len(node_ids)
            else:
                ans = BFS(graph, len(graph.keys()), start, ttl)
            print("Case {}: {} nodes not reachable from "
                  "node {} with TTL = {}.".format(query_num, ans, start, ttl))


if __name__ == '__main__':
    main()
