# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11518.pdf
directed graph
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())

    n_case = int(next(recs))
    for _ in range(n_case):
        n_domino, n_edge, n_ko = list(map(int, next(recs).split()))
        graph = [set() for _ in range(n_domino)]
        visited = [False for _ in range(n_domino)]
        for _ in range(n_edge):
            n1, n2 = list(map(lambda x: int(x) - 1, next(recs).split()))
            graph[n1].add(n2)

        total_count = 0
        for _ in range(n_ko):
            start = int(next(recs).strip()) - 1
            if visited[start]:
                continue

            stack = [start, ]
            visited[start] = True
            count = 1
            while stack:
                node = stack.pop()
                for child in graph[node]:
                    if not visited[child]:
                        stack.append(child)
                        visited[child] = True
                        count += 1
            total_count += count

        print(total_count)


if __name__ == '__main__':
    main()
