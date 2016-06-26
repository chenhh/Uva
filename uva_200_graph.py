# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/2/200.pdf
topological sort
"""

import sys


def topological_sort(graph, n_node):
    orders = []
    candidate_roots = set(graph.keys())
    for _ in range(n_node):
        node_have_in_edges = set()
        for node in candidate_roots:
            for e in graph[node]:
                if e in candidate_roots:
                    node_have_in_edges.add(e)
        roots = list(candidate_roots - node_have_in_edges)
        candidate_roots = node_have_in_edges
        orders.extend(roots)
        if len(orders) >= n_node:
            break

    if len(orders) < n_node:
        raise ValueError('there is a cycle in the graph.')

    return "".join(reversed(orders))


def main():
    recs = iter(sys.stdin.readlines())
    graph = {}
    data = []
    while True:
        try:
            line = next(recs).strip()
            if line != '#':
                data.append(line)
            else:
                for idx in range(1, len(data)):
                    prev, curr = data[idx - 1], data[idx]
                    cmp_len = min(len(prev), len(curr))
                    for kdx in range(cmp_len):
                        graph.setdefault(prev[kdx], [])
                        graph.setdefault(curr[kdx], [])
                        if prev[kdx] != curr[kdx]:
                            graph[curr[kdx]].append(prev[kdx])
                            break
                # print (graph)
                print(topological_sort(graph, len(graph)))

                graph.clear()
                data.clear()

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
