# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/105/10507.pdf

BFS, in each queue pop, count the degree of un-waked nodes
connected with the waked nodes.
After the queue is empty, add all nodes whose degree >=3 to the queue.
The procedure is repeated until all nodes are visited.
"""

import sys
from collections import deque


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        try:
            while True:
                data = next(recs).strip()
                if data:
                    n_node = int(data)
                    break
            graph = {}
            n_edge = int(next(recs))
            wakes = set(next(recs).strip())
            for n in wakes:
                graph.setdefault(n, [])

            for _ in range(n_edge):
                n1, n2 = list(next(recs).strip())
                graph.setdefault(n1, []).append(n2)
                graph.setdefault(n2, []).append(n1)

            if len(wakes) < 3 or len(graph.keys()) < n_node:
                # no enough waked regions or there are some areas are isolated.
                print("THIS BRAIN NEVER WAKES UP")
                continue

            # print (graph)
            # BFS
            queue = deque()
            waked = {k: 0 for k in graph.keys()}
            waked_set = set()
            for n in wakes:
                waked[n] = 3
                waked_set.add(n)
                queue.append(n)

            year = 0
            while queue:
                # the node is a waked area.
                node = queue.popleft()
                # print (node)
                for child in graph[node]:
                    if waked[child] < 3:
                        waked[child] += 1

                waked_set.add(node)
                if len(waked_set) == n_node:
                    # all areas are waked
                    print("WAKE UP IN, {}, YEARS".format(year))
                    break

                # there are some un-waked area.
                if not queue:
                    new_wake_area = False
                    for n in graph.keys():
                        if waked[n] < 3:
                            # an un-waked area, reset link count
                            waked[n] = 0
                        else:
                            # an waked area
                            if n not in waked_set:
                                new_wake_area = True
                            queue.append(n)
                    if new_wake_area:
                        # reset n_waked
                        waked_set.clear()
                        year += 1
                    else:
                        print("THIS BRAIN NEVER WAKES UP")
                        break

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
