# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/2/280.pdf

the 0 represents the end of edge may not in the same line with the start
vertex.
"""

import sys


def dfs(graph, n_node, start):
    """ the node i is not visited unless there is a path from node j """
    stack = [start, ]
    visited = [False] * n_node
    while len(stack) > 0:
        node = stack.pop()
        for child in graph[node]:
            if not visited[child]:
                stack.append(child)
                # there is a edge from node to child.
                visited[child] = True

    if all(visited):
        return 0
    else:
        unreached = [str(idx + 1) for idx, v in enumerate(visited) if not v]
        unreached.insert(0, str(len(unreached)))
        return " ".join(unreached)


def main():
    recs = iter(sys.stdin.readlines())
    while 1:
        try:
            n_node = int(next(recs))
            graph = [[] for _ in range(n_node)]
            # Each possible start vertex will appear once or not at all.
            while 1:
                # assume the edges are in the same line
                vals = list(map(int, (next(recs).split())))
                assert (vals[-1] == 0)
                if vals[0] == 0:
                    break
                graph[vals[0] - 1] = [v - 1 for v in vals[1:-1]]
            # print (graph)
            data = list(map(int, (next(recs).split())))
            starts = [v - 1 for v in data[1:]]

            for s in starts:
                ans = dfs(graph, n_node, s)
                print(ans)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
