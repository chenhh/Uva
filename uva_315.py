# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/3/315.pdf
http://luckycat.kshs.kh.edu.tw/homework/q315.htm

[
    [1,4,5],
    [0, 2],
    [1],
    [1,4],
    [0,3],
    [0,6,7],
    [5,7],
    [6,8,9],
    [7],
    [7],
]
"""

import sys

def articulation_point(graph, n_node, start=0):
    """ graph: edge list
    the root having two or more sub-trees must be an articulation point,
    because there is no alternative path from left sub-trees to right-subtrees.
    """
    # (parent, node)
    stack = [start, ]
    visited = [-1] * n_node
    parents = [-1] * n_node
    lows = [-1] * n_node
    n_children = [0] * n_node
    step = 1
    while stack:
        node = stack.pop()
        if visited[node] == -1:
            # the dfs tree edge
            visited[node] =step
            lows[node] = step
            step += 1
            # a valid tree edge (both parent and child are visited)
            if parents[node] >= 0:
                n_children[parents[node]] += 1
                lows[parents[node]] = min(lows[node], lows[parents[node]])
            for child in graph[node]:
                if visited[child] == -1:
                    # the same child may be added to the stack multiple
                    # times, and only the first one pop from the stack is the
                    # valid child of the parent.
                    # Some (parent, child) pair may not be visited in the
                    # future.
                    stack.append(child)
                    parents[child] = node
                else:
                    # back edge (both parent and child are visited)
                    lows[node] = min(lows[node], visited[child] )
        print ("node:", node)
        print ("Stack:", stack)
        print("visited:", visited)
        print("low:", lows)
        print("parent:", parents)

    for idx in range(n_node):
        for jdx in range(n_node):
            if (idx != start and parents[jdx] == idx and
                        lows[jdx] >= visited[idx]):
                print ("ap:", idx)


    print ("graph:",graph)
    print ("visited:", visited)
    print("low:", lows)
    print ("parent:", parents)
    print ("n_child:",n_children)





def main():
    recs = iter(sys.stdin.readlines())
    while 1:
        n_node = int(next(recs))
        if n_node == 0:
            break
        # undirected graph
        graph = [[] for _ in range(n_node) ]
        for _ in range(n_node):
            data = next(recs).strip()
            if data == '0':
                break
            edges = list(map(int, data.split()))
            parent, children = edges[0], edges[1:]
            for child in children:
                graph[parent-1].append(child-1)
                graph[child-1].append(parent-1)

        articulation_point(graph, n_node)
if __name__ == '__main__':
    # main()
    graph = [
        [1, 4, 5],
        [0, 2, 3],
        [1],
        [1, 4],
        [0, 3],
        [0, 6, 7],
        [5, 7],
        [6, 8, 9],
        [7],
        [7]]
    print(articulation_point(graph, len(graph), 1))
