# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/109/10986.pdf

Dijkstra algorithm
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
example:
1
7 10 0 6
0 1 32
0 5 3
1 5 7
2 5 2
1 2 21
1 4 12
2 4 6
2 6 11
4 3 13
3 6 9

ans: [0, 10, 5, 24, 11, 3, 16]
"""

import heapq
import sys


def Dijkstra_queue(graph, n_node, src, tgt):
    """
    Dijkstra algorithm implemented using the priority queue
    """
    INF = 2 << 31
    visited = [False] * n_node
    # store the distance from src to all other nodes
    dist = [INF] * n_node
    dist[src] = 0
    # (dist, node), the queue will adjust by dist.
    queue = [(0, src), ]
    q_push, q_pop = heapq.heappush, heapq.heappop

    while queue:
        # choose the node with the smallest distance
        n_dist, node = q_pop(queue)
        visited[node] = True

        for child in graph[node]:
            dist_node_child = graph[node][child]
            if (not visited[child] and
                            dist[node] + dist_node_child < dist[child]):
                dist[child] = dist[node] + dist_node_child
                q_push(queue, (dist[child], child))

    # print (dist)
    return dist[tgt] if dist[tgt] != INF else "unreachable"


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for tdx in range(n_case):
        while True:
            data = next(recs).strip()
            if data:
                n_node, n_edge, src, tgt = list(map(int, data.split()))
                break
        graph = [{} for _ in range(n_node)]
        for _ in range(n_edge):
            s, t, w = list(map(int, next(recs).split()))
            # if there are multiple link between src and tgt, choose
            # the minimum value.
            if t not in graph[s].keys():
                graph[s][t] = w
            else:
                if w < graph[s][t]:
                    graph[s][t] = w

            if s not in graph[t].keys():
                graph[t][s] = w
            else:
                if w < graph[t][s]:
                    graph[t][s] = w

        ans = Dijkstra_queue(graph, n_node, src, tgt)
        print("Case #{}: {}".format(tdx + 1, ans))


if __name__ == '__main__':
    main()
