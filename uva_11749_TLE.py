# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/117/11749.pdf
the IO of the edge (without graph.append) requires 2.390 secs.
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())

    stack = []
    stack_clear = stack.clear
    stack_append = stack.append
    stack_pop = stack.pop
    split = str.split

    while True:
        n_node, n_edge = list(map(int, next(recs).split()))
        if not n_node:
            break
        N_INF = -2 << 32
        graph = [[N_INF] * n_node for _ in range(n_node)]
        visited = [False] * n_node
        stack_clear()

        max_ppa = -2 << 32
        for _ in range(n_edge):
            # the IO of the edge (without graph.append) requires 2.390 secs.
            # with graph (adjacency) operation requires 2.90 secs.
            # with graph (edge list) operation will TLE.
            n1, n2, ppa = list(map(int, split(next(recs))))
            n1, n2 = n1 - 1, n2 - 1
            graph[n1][n2] = ppa
            graph[n2][n1] = ppa
            if ppa > max_ppa:
                max_ppa, max_n1, max_n2 = ppa, n1, n2

        # first element
        stack_append((max_n1, max_n2))
        visited[max_n1] = visited[max_n2] = True
        n_city = 2

        max_city = 0
        while stack:
            n1, n2 = stack_pop()
            for child1, ppa1 in enumerate(graph[n1]):
                if not visited[child1] and ppa1 == max_ppa:
                    stack_append((n1, child1))
                    visited[child1] = True
                    n_city += 1

            for child2, ppa2 in enumerate(graph[n2]):
                if not visited[child2] and ppa2 == max_ppa:
                    stack_append((n2, child2))
                    visited[child2] = True
                    n_city += 1

            if not stack:
                max_city = max(max_city, n_city)
                n_city = 0
                for n1 in range(n_node):
                    if visited[n1]:
                        continue
                    if stack:
                        break
                    for n2, ppa2 in enumerate(graph[n2]):
                        if not visited[n2] and ppa2 == max_ppa:
                            stack_append((n1, n2))
                            visited[n1] = visited[n2] = True
                            n_city += 2
                            break
        print(max_city)


if __name__ == '__main__':
    main()
