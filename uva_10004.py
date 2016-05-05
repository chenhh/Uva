# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/100/10004.pdf
- no node will have an edge to itself
- the graph is nondirected
- • the graph will be strongly connected
graph + DFS or BFS
4
3
0 3
1 2
2 3
0
BICOLORABLE

"""

def dfs_iterative(graph, start_node):
    # print (graph)
    stack = [start_node,]
    n_node = len(graph)
    walked = [False] * n_node
    seqs = []

    bicolor = True
    while len(stack) > 0:
        node = stack.pop()
        if not walked[node]:
            walked[node] = True
            seqs.append(node)
            for child in graph[node]:
                stack.append(child)
    print (seqs)
    return bicolor

def main():
    while True:
        n_node = int(input())
        if n_node == 0:
            break

        graph = [[] for _ in range(n_node)]
        n_edge = int(input())
        for _ in range(n_edge):
            n1, n2 = list(map(int, input().split()))
            # undirected
            graph[n1].append(n2)
            graph[n2].append(n1)

        bicolor = dfs_iterative(graph, 0)

        if not bicolor:
            print ("NOT BICOLORABLE.")
        else:
            print ("BICOLORABLE.")

if __name__ == '__main__':
    main()





