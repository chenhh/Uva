# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/7/762.pdf
http://luckycat.kshs.kh.edu.tw/homework/q762.htm

the blank line between two case (not print for last case)
will case the WA.
"""

import sys
from collections import deque


def bfs(graph, n_node, src, tgt):
    """ graph: dict of list """

    if src == tgt:
        # if the src is the same with the tgt, return it without regard
        # the src is in graph or not.
        return [src, tgt]

    if src not in graph.keys() or tgt not in graph.keys():
        return None

    visited = {k: False for k in graph.keys()}
    parents = {k: -1 for k in graph.keys()}
    queue = deque([src, ])
    visited[src] = True
    is_connected = False

    while queue:
        node = queue.popleft()
        if node == tgt:
            is_connected = True
            break
        for child in graph[node]:
            if visited[child] is False:
                queue.append(child)
                parents[child] = node
                visited[child] = True

    if not is_connected:
        return None

    # traceback
    path, curr = [], tgt
    while curr != -1:
        path.append(curr)
        curr = parents[curr]

    return path[::-1]


def main():
    recs = iter(sys.stdin.readlines())
    case = 0

    while True:
        try:
            while True:
                data = next(recs).strip()
                if data:
                    n_edge = int(data)
                    break

            graph = {}
            for _ in range(n_edge):
                n1, n2 = next(recs).split()
                graph.setdefault(n1, []).append(n2)
                graph.setdefault(n2, []).append(n1)

            src, tgt = next(recs).split()

            if case:
                print()

            case += 1
            ans = bfs(graph, len(graph.keys()), src, tgt)
            if ans is None:
                print("No route")
            else:
                assert len(ans) >= 2
                assert ans[0] == src
                assert ans[-1] == tgt
                for idx in range(1, len(ans)):
                    print("{} {}".format(ans[idx - 1], ans[idx]))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
