# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

11080 - Place the Guards

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/110/11080.pdf

bipartite_graph, there may be many components in the graph.
in each components,
we first test the components is a bipartite graph or not.
if the component is a a bipartite graph, then the number of guards is the
color which has smaller numbers than the other colors.
"""

import sys
from collections import deque


def bipartite_graph(graph, n_node, n_edge):
    if n_edge == 0:
        # isolate nodes
        return n_node

    # -1: no-color, 0: black, 1: white
    colors = [-1] * n_node
    visited = [False] * n_node
    n_colors = [0] * 2

    stack = deque([0])
    visited[0] = True
    colors[0] = 0
    n_colors[0] = 1
    n_guard = 0
    stack_append = stack.append
    stack_pop = stack.pop

    while stack:
        curr = stack_pop()
        for child in graph[curr]:
            if not visited[child]:
                visited[child] = True
                stack_append(child)
                colors[child] = 1 - colors[curr]
                n_colors[colors[child]] += 1
            else:
                # the child is visited and the same color as curr node
                if colors[child] >= 0 and colors[child] != 1 - colors[curr]:
                    return -1

        if not stack:
            # search next components
            if n_colors[0] and not n_colors[1]:
                # only black color is used
                n_guard += n_colors[0]
            elif not n_colors[0] and n_colors[1]:
                # only white color is used
                n_guard += n_colors[1]
            else:
                # both color are used
                n_guard += min(n_colors)

            # reset colors
            n_colors[0] = 0
            n_colors[1] = 0

            for idx, v in enumerate(visited):
                if not v:
                    stack_append(idx)
                    visited[idx] = True
                    colors[idx] = 0
                    n_colors[0] = 1
                    break

    return n_guard


def main():
    recs = iter(sys.stdin.readlines())

    n_case = int(next(recs))
    while n_case:
        n_node, n_edge = list(map(int, next(recs).split()))
        # undirected graph
        graph = [[] for _ in range(n_node)]

        for _ in range(n_edge):
            src, tgt = list(map(int, next(recs).split()))
            graph[src].append(tgt)
            graph[tgt].append(src)

        print("{}".format(bipartite_graph(graph, n_node, n_edge)))

        # update
        n_case -= 1


if __name__ == '__main__':
    main()
