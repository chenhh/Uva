# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10926.pdf
"""

import sys
from collections import deque


def main():
    recs = iter(sys.stdin.readlines())
    stack = deque()
    stack_clear = stack.clear
    stack_append = stack.append
    stack_pop = stack.pop

    while True:
        n_node = int(next(recs))
        if not n_node:
            break
        graph = [[] for _ in range(n_node)]

        for ndx in range(n_node):
            task = list(map(int, next(recs).split()))
            if task[0] == 0:
                continue
            graph[ndx].extend(list(map(lambda x: x - 1, task[1:])))
        # print (graph)

        max_node = 0
        max_n_traversal_node = 0
        for ndx in range(n_node):
            if not graph[ndx]:
                # the node is not depend on other nodes.
                continue
            visited = [False] * n_node
            n_traversal_node = 0

            stack_clear()
            stack_append(ndx)
            visited[ndx] = True
            n_traversal_node += 1
            while stack:
                node = stack_pop()
                for child in graph[node]:
                    if not visited[child]:
                        stack_append(child)
                        visited[child] = True
                        n_traversal_node += 1
            if n_traversal_node > max_n_traversal_node:
                max_n_traversal_node = n_traversal_node
                max_node = ndx
        print(max_node + 1)


if __name__ == '__main__':
    main()
