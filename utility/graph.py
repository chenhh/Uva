# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

def dfs_iterative(graph, start_node):
    """
    the graph contains node from 0 ~ (n-1)
    assume the graph will be strongly connected

    Parameters:
    -----------------------
    graph: list of list, graph[idx] contains the list of edges
    start_node，integer, the dfs start node

    Return:
    -----------------------
    sequences: list, the sequence of DFS traversal
    """
    stack = [start_node,]
    walked = [False] * len(graph)
    sequences = []

    while len(stack) > 0:
        node = stack.pop()
        if not walked[node]:
            print (node)
            sequences.append(node)
            for child in graph[node]:
                stack.append(child)

    return sequences