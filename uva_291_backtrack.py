# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/2/291.pdf
http://luckycat.kshs.kh.edu.tw/homework/q291.htm

because the graph is an 2-d list, if we use stack to simulate the recursion,
we have to use copy.deepcopy to pass the graph.
"""
graph = [[False] * 5 for _ in range(5)]
graph[0][1] = graph[1][0] = True
graph[0][2] = graph[2][0] = True
graph[0][4] = graph[4][0] = True
graph[1][2] = graph[2][1] = True
graph[1][4] = graph[4][1] = True
graph[2][3] = graph[3][2] = True
graph[2][4] = graph[4][2] = True
graph[3][4] = graph[4][3] = True

path = [-1] * 9


def dfs(node, n_path):
    global graph, path
    path[n_path] = node
    if n_path == 8:
        print("".join(str(v + 1) for v in path))
        return

    for idx in range(5):
        if graph[node][idx]:
            graph[node][idx] = graph[idx][node] = False
            dfs(idx, n_path + 1)
            graph[node][idx] = graph[idx][node] = True


def main():
    dfs(0, 0)


if __name__ == '__main__':
    main()
