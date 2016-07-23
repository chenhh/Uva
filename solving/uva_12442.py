# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: working
difficulty: 2

https://uva.onlinejudge.org/external/124/12442.pdf
http://luckycat.kshs.kh.edu.tw/homework/q12442.htm
directed graph, may containing cycle
"""

import sys


def dfs_variant(graph, n_node):
    """
    graph: dict of list
    if there is a node which can traversal all other nodes, then
    the node is the solution.
    if there are no any node can traversal all nodes, the the node
    which can traversal the most nodes is the solution.
    correct, but TLE
    """
    # ascending node ids.
    nodes = list(graph.keys())
    n_visited_nodes = {k: 0 for k in nodes}

    for start in nodes:
        visited = {k: False for k in nodes}
        stack = [start, ]
        visited[start] = True
        while stack:
            curr = stack.pop()
            for child in graph[curr]:
                if not visited[child]:
                    stack.append(child)
                    visited[child] = True

            if not stack:
                n_visited = sum(visited.values())
                n_visited_nodes[start] = n_visited

    # no any node can visit all nodes
    max_node_idx, max_node = 0, 0
    for ndx, n_node in n_visited_nodes.items():
        if n_node > max_node:
            max_node = n_node
            max_node_idx = ndx
    return max_node_idx


def dfs_variant2(graph, n_node, start):
    """
    graph: dict of list
    """

    visited = {k: False for k in graph.keys()}
    stack = [start, ]
    visited[start] = True
    while stack:
        curr = stack.pop()
        for child in graph[curr]:
            if not visited[child]:
                stack.append(child)
                visited[child] = True

    n_visited = sum(visited.values())
    return start, n_visited


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        graph = {}
        n_edge = int(next(recs))
        for _ in range(n_edge):
            n1, n2 = list(map(int, next(recs).split()))
            graph.setdefault(n1, []).append(n2)
        # print (graph)
        ans = dfs_variant(graph, len(graph.keys()))
        print("Case {}: {}".format(tdx + 1, ans))


def parallel_main():
    from multiprocessing import Pool
    from time import time
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for tdx in range(n_case):
        t1 = time()
        graph = {}
        n_edge = int(next(recs))
        for _ in range(n_edge):
            n1, n2 = list(map(int, next(recs).split()))
            graph.setdefault(n1, []).append(n2)

        n_node = len(graph.keys())
        pool = Pool()
        results = [pool.apply(dfs_variant2, (graph, n_node, start))
                   for start in graph.keys()]
        n_visited_nodes = [r for r in results]
        # no any node can visit all nodes
        max_node_idx, max_node = 0, 0
        for ndx, n_node in n_visited_nodes:
            if n_node > max_node:
                max_node = n_node
                max_node_idx = ndx

        print("Case {}: {}".format(tdx + 1, max_node_idx))


if __name__ == '__main__':
    # main()
    parallel_main()
