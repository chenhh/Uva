# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/103/10305.pdf
topological sort
"""

import sys


def topological_sort(graph, n_node):
    """ graph: edge list """

    orders = []
    candidate_roots = set(range(n_node))

    while len(orders) < n_node:
        node_have_in_edges = set()
        for sdx, edges in enumerate(graph):
            if sdx not in candidate_roots:
                # the node is a root, skip
                continue
            for e in edges:
                if e in candidate_roots:
                    node_have_in_edges.add(e)
        roots = sorted(list(candidate_roots - node_have_in_edges))
        orders.extend(roots)
        candidate_roots = node_have_in_edges

    return " ".join(str(v + 1) for v in orders)


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        n_node, n_edge = list(map(int, next(recs).split()))
        if not n_node:
            break
        # directed graph
        graph = [[] for _ in range(n_node)]
        for _ in range(n_edge):
            src, tgt = list(map(int, next(recs).split()))
            graph[src - 1].append(tgt - 1)

        print(topological_sort(graph, n_node))


if __name__ == '__main__':
    main()
