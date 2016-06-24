# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 3

https://uva.onlinejudge.org/external/1/104.pdf
http://luckycat.kshs.kh.edu.tw/homework/q104.htm

variant Floyd–Warshall algorithm
time complexity: O(n^4)
"""

import sys


def arbitrage(graph, n_node):
    """
    graph: adjacency matrix

    Floyd-Warshall algorithm:
        d[k][i][j] = min(d[k-1][i][j], d[k-1][i][k] + d[k-1][k][j])
        d[k][i][j]: the shortest path from  node i to node j considering
        node k is the min distance between.
            - d[k-1][i][j]: the path from node i to node j without
                            passing node k.
            - d[k-1][i][k] + d[k-1][k][j]: the path from node i to node k plus
                                           the path from node k to node j.
    note: when k-1=-1, d[-1][i][j] is the adjacency matrix of the graph.

    d[k][i][j] = max(d[k-1][i][j], d[k-1][i][s]*graph[s][j])
    d[k][i][j]: the profit of kth exchange from currency i to currency j is
        the maximum profit of
        - d[k-1][i][j]: the profit of (k-1)th exchange from currency i to
                        currency j.
        - d[k-1][i][s]*graph[s][j]: the profit of (k-1)th exchange from
                        currency i to currency s, then from currency s to
                        currency j.
    note: d[0][i][j] is the adjacency of the graph.

    path[k][i][j]: the kth node of the path from ith currency to jth
                    currency.
    """
    # initialize
    # (kdx, idx, jdx), shape: (n_node)*(n_node)* (n_node)
    wealth = [[[1] * n_node for _ in range(n_node)]
              for _ in range(n_node)]
    path = [[[-1] * n_node for _ in range(n_node)]
            for _ in range(n_node)]
    for idx in range(n_node):
        for jdx in range(n_node):
            wealth[0][idx][jdx] = graph[idx][jdx]

    # num. of exchange
    for kdx in range(1, n_node):
        # src currency
        for idx in range(n_node):
            # tgt currency
            for jdx in range(n_node):
                # not exchange and it does not need to record the path
                wealth[kdx][idx][jdx] = wealth[kdx - 1][idx][jdx]

                # middle currency
                for sdx in range(n_node):
                    indirect = (wealth[kdx - 1][idx][sdx]
                                * wealth[0][sdx][jdx])
                    if wealth[kdx][idx][jdx] < indirect:
                        # there is a exchange earning higher profit
                        wealth[kdx][idx][jdx] = indirect
                        path[kdx][idx][jdx] = sdx

        for idx in range(n_node):
            if wealth[kdx][idx][idx] > 1.01:
                return path_traceback(path, kdx, idx)

    # no arbitrage
    return "no arbitrage sequence exists"


def path_traceback(path, kdx, idx):
    stack = [(kdx, path[kdx][idx][idx])]
    ans = [idx, ]
    while stack:
        step, prev_node = stack.pop()
        if prev_node != -1:
            ans.append(prev_node)
            stack.append((step - 1, path[step - 1][idx][prev_node]))
    ans.append(idx)

    return " ".join(str(v + 1) for v in reversed(ans))


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        try:
            n_node = int(next(recs))
            graph = [[] * n_node for _ in range(n_node)]
            for idx in range(n_node):
                rates = list(map(float, next(recs).split()))
                graph[idx] = rates[:idx] + [1] + rates[idx:]
            ans = arbitrage(graph, n_node)
            print(ans)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
