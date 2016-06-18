# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""
def dfs_bicolor(graph, start_node):
    # print (graph)
    stack = [start_node,]
    n_node = len(graph)
    colors= [-1] * n_node
    colors[start_node] = 0
    walked = [False] * n_node
    bicolor = True

    while len(stack) > 0:
        node = stack.pop()
        if not bicolor:
            break

        if not walked[node]:
            walked[node] = True
            for child in graph[node]:
                if colors[child] == -1:
                    colors[child] = 1 - colors[node]
                elif colors[child] != 1 - colors[node]:
                    bicolor = False
                    break
                stack.append(child)
    return bicolor


def coloring(graph, n_node):
    queue = [0, ]
    colors = [-1] * n_node
    colors[0] = 0
    visited = [False] * n_node

    while len(queue) > 0:
        node = queue.pop()
        if not visited[node]:
            visited[node] = True
            for child in graph[node]:
                # find used colors
                used = frozenset(colors[neighbor] for neighbor in graph[child]
                                 if colors[neighbor] != -1)

                # the worst case is that all nodes are in different colors.
                for cdx in range(n_node):
                    if cdx not in used:
                        colors[child] = cdx
                        break
                queue.append(child)


def coloring(graph, n_node):
    """
    uva 193,
    backtracking coloring, the black node can't be neighbor of a black node,
    but the white node can be neighbor of all nodes.
    the graph may contain isolated nodes or disconnected components.
    0 is white, 1 is black
    """
    max_n_black, black_nodes = 0, None

    # the first node can be a white or a black node.
    stack = [(0, [0] + [-1] * (n_node - 1)), (0, [1] + [-1] * (n_node - 1))]
    while stack:
        node, n_colors = stack.pop()
        if node >= n_node:
            # assert sum(1 for c in n_colors if c == -1) == 0
            n_black = sum(n_colors)
            if n_black > max_n_black:
                max_n_black = n_black
                black_nodes = [str(idx + 1) for idx, c in enumerate(n_colors)
                               if c == 1]
            continue
        # test if the current can be a black node.
        black_used = [n_colors[neighbor]
                      for neighbor in graph[node]
                      if n_colors[neighbor] == 1]
        if not black_used:
            # the node can be a black node, the n_colors should copy by value
            n_colors[node] = 1
            stack.append((node + 1, n_colors[:]))
        # backtrack, and the node must can be a white node
        n_colors[node] = 0
        stack.append((node + 1, n_colors[:]))

    return (max_n_black, black_nodes)
