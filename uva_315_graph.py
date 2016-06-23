# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 3

https://uva.onlinejudge.org/external/3/315.pdf
http://luckycat.kshs.kh.edu.tw/homework/q315.htm

note, the graph may be disconnected.
"""

import sys


def articulation_points(graph, n_node, roots=[0, ]):
    """ graph: edge list
    the root having two or more sub-trees must be an articulation point,
    because there is no alternative path from left sub-trees to right-subtrees.
    """
    # (parent, node)
    stack = [roots[0], ]
    components = [-1] * n_node
    com_id = 0
    visited = [-1] * n_node
    parents = [-1] * n_node
    lows = [-1] * n_node
    n_child = [0] * n_node
    step = 1

    while stack:
        node = stack.pop()
        if visited[node] == -1:
            # not visited, dfs tree edge
            visited[node] =step
            lows[node] = step
            components[node] = com_id
            step += 1
            # the node is not root of dfs tree.
            if parents[node] >= 0:
                n_child[parents[node]] += 1

            for child in reversed(graph[node]):
                if visited[child] == -1:
                    # the same child may be added to the stack multiple
                    # times, and only the first one pop from the stack is the
                    # valid child of the parent.
                    stack.append(child)
                    parents[child] = node
                else:
                    # back edge, because the child is visited and
                    # it is not parent of the node.
                    if parents[node] != child:
                        lows[node] = min(lows[node], visited[child])

                        # traceback from node to the child node
                        curr = parents[node]
                        while curr != child:
                            lows[curr] = min(lows[curr], lows[node])
                            curr = parents[curr]
        if not stack:
            # for disconnected points
            for idx, val in enumerate(visited):
                if val == -1:
                    stack.append(idx)
                    roots.append(idx)
                    com_id += 1
                    break

    articulations = set()
    for rdx, root in enumerate(roots):
        # for root node
        if n_child[root] >= 2:
            articulations.add(root)
        for ndx, pdx in enumerate(parents):
            # non-root nodes and in the same components
            if (components[ndx] == rdx and pdx >= 0 and pdx != root and
                        lows[ndx] >= visited[pdx]):
                articulations.add(pdx)

    return (articulations, visited)


def test_ap():
    # http://www.csie.ntnu.edu.tw/~u91029/Component.html#1
    graph = [
        [1, 4, 5],
        [0, 2, 3],
        [1],
        [1, 4],
        [0, 3],
        [0, 6, 7],
        [5, 7],
        [5, 6, 8, 9],
        [7],
        [7]]
    # the points is {0,1,5,7}
    print(articulation_points(graph, len(graph), 0))


def main():
    recs = iter(sys.stdin.readlines())
    while 1:
        try:
            n_node = int(next(recs))
            if n_node == 0:
                raise GeneratorExit
            # undirected graph
            graph = [[] for _ in range(n_node)]
            for _ in range(n_node + 1):
                data = next(recs).strip()
                if data == '0':
                    break
                edges = list(map(int, data.split()))
                parent, children = edges[0], edges[1:]
                for child in children:
                    graph[parent - 1].append(child - 1)
                    graph[child - 1].append(parent - 1)

            aps, visited = articulation_points(graph, n_node)
            print(len(aps))
        except (StopIteration, GeneratorExit):
            break


if __name__ == '__main__':
    main()
