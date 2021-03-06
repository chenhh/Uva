# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def bfs(graph, n_node, start, ttl):
    """ uva 336, the graph is a dict of list """
    from collections import deque
    visited = {k: False for k in graph.keys()}
    depth = {k: -1 for k in graph.keys()}
    parents = {k: -1 for k in graph.keys()}
    # (parent, node)
    queue = deque([(start, start), ])

    while queue:
        parent, node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            parents[node] = parent
            if depth[parent] >= ttl:
                break
            depth[node] = depth[parent] + 1

            for child in graph[node]:
                if not visited[child]:
                    queue.append((node, child))

    return (sum(1 for _, v in depth.items() if v == -1))


def bfs2(graph, n_node, start, ttl):
    """ uva336 the graph is a dict of list """
    visited = {k: False for k in graph.keys()}
    depth = {k: -1 for k in graph.keys()}
    parents = {k: -1 for k in graph.keys()}
    # (parent, node)
    queue = deque([start, ])
    visited[start] = True
    parents[start] = start

    while queue:
        node = queue.popleft()
        parent = parents[node]
        if depth[parent] >= ttl:
            break
        depth[node] = depth[parent] + 1
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
                parents[child] = node
                visited[child] = True

    return (sum(1 for _, v in depth.items() if v == -1))


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


def connected_components(graph, n_node):
    """ uva 572,352 459, dfs search,
     graph is shown in edge list
     """
    if n_node == 0:
        return 0
    stack = [0, ]
    visited = [False] * n_node

    n_sub = 1
    while not all(visited):
        # print ("Stack:", stack)
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for child in graph[node]:
                if not visited[child]:
                    stack.append(child)
        if not stack:
            for idx, val in enumerate(visited):
                if not val:
                    stack.append(idx)
                    n_sub += 1
                    break
    return n_sub


def connected_components_dfs(image, rdx, cdx, dim):
    """
    uva 352, another way to count connected components.
    the image is call by reference, and mark all connected components to zero.
    the image is a adjacency matrix.
    """
    # N, NE, E, SE, S, SW, W, NW
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    stack = [(rdx, cdx)]
    while stack:
        x, y = stack.pop()
        if image[x][y] == '1':
            image[x][y] = '0'
            for h, v in directions:
                if 0 <= x + h < dim and 0 <= y + v < dim:
                    stack.append((x + h, y + v))


def connected_components_region(region, n_row, n_col):
    """
    uva 10336, connected components of different part in the regions
    """
    # N, E, S, W
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    lang_cnt = {region[0][0]: 1}
    lang_get = lang_cnt.get

    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if 'a' <= region[x][y] <= 'z':
            lang = region[x][y]
            region[x][y] = region[x][y].upper()
            for h, v in directions:
                if (0 <= x + h <= n_row - 1 and 0 <= y + v <= n_col - 1 and
                            region[x + h][y + v] == lang):
                    stack.append((x + h, y + v))

        # find next region
        if not stack:
            for rdx, row in enumerate(region):
                if stack:
                    break
                for cdx, c in enumerate(row):
                    if 'a' <= c <= 'z':
                        stack.append((rdx, cdx))
                        lang_cnt[region[rdx][cdx]] = (
                            lang_get(region[rdx][cdx], 0) + 1)
                        break

    return lang_cnt



def queens(n_queen=8):
    """
    backtracking, searching by row first then by column.
    the size of the board is n_row * n_col (rdx from 0 to n_row -1 (n_col - 1)
    if there is a queen placed in board[rdx][cdx], then
        the rdx row, the cdx column, the diagonal (rdx+cdx)%(2*(n_col)-1), and
        the diagonal ((rdx-cdx)+(2*(n_col)-1))%((2*(n_col)-1) can't place
        another queen.

    q1: (x1, y1), q2:(x2, y2), if q1 and q2 are in the same diagonal,
    then abs( x1-x2) == abs(y1-y2)
    e.g. q1: (1, 2), then
        left diagonal :[(0,1), (2,3), (3,4), (4,5), (6,7]
        right diagonal :[(2,0), (0,3)]
        can't place another queen.

    """
    # square chessboard
    n_row = n_col = n_queen
    diagonal_size = (2 * n_col - 1)
    ans = []

    # (rdx, cdx, rows, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, 0, [False] * n_row, [False] * n_col,
              [False] * diagonal_size, [False] * diagonal_size, [])]

    while stack:
        # column first, then by row
        rdx, cdx, rows, cols, left, right, positions = stack.pop()
        # print (rdx, cdx, queen_num)
        if rdx >= n_row:
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        if rdx < n_row and len(positions) < rdx - 1:
            # in rdx row, it should has rdx-1 or rdx queens
            # prune the impossible path
            continue

        if cdx >= n_col:
            # start from the first column of next row
            stack.append((rdx + 1, 0, rows[:], cols[:], left[:], right[:],
                          positions[:]))
            continue

        # place the queen
        l_idx = (rdx + cdx) % diagonal_size
        r_idx = (rdx - cdx + diagonal_size) % diagonal_size
        if (not rows[rdx] and not cols[cdx] and not left[l_idx]
            and not right[r_idx]):
            # the position can place a new queen
            rows[rdx], cols[cdx] = True, True
            left[l_idx], right[r_idx] = True, True

            stack.append((rdx, cdx + 1, rows[:], cols[:], left[:], right[:],
                          positions + [(rdx, cdx)]))
            rows[rdx], cols[cdx] = False, False
            left[l_idx], right[r_idx] = False, False
        # the position does not place a new queen
        stack.append((rdx, cdx + 1, rows[:], cols[:], left[:], right[:],
                      positions[:]))

    return ans


def queens_iterative(n_queen=8):
    """
    uva 167
    backtracking, searching by row first then by column.
    the size of the board is n_row * n_col (rdx from 0 to n_row -1 (n_col - 1)
    if there is a queen placed in board[rdx][cdx], then
        the rdx row, the cdx column, the diagonal (rdx+cdx)%(2*(n_col)-1), and
        the diagonal ((rdx-cdx)+(2*(n_col)-1))%((2*(n_col)-1) can't place
        another queen.

    q1: (x1, y1), q2:(x2, y2), if q1 and q2 are in the same diagonal,
    then abs( x1-x2) == abs(y1-y2)
    e.g. q1: (1, 2), then
        left diagonal :[(0,1), (2,3), (3,4), (4,5), (6,7]
        right diagonal :[(2,0), (0,3)]
        can't place another queen.

    """
    # square chessboard
    n_row = n_col = n_queen
    d_size = (2 * n_col - 1)
    ans = []

    # (rdx, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, [False] * n_col, [False] * d_size, [False] * d_size, [])]

    while stack:
        # scanning by row
        rdx, cols, lefts, rights, positions = stack.pop()
        if rdx >= n_row:
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        for cdx in range(n_col):
            l_idx, r_idx = (rdx + cdx) % d_size, (rdx - cdx) % d_size
            if not any((cols[cdx], lefts[l_idx], rights[r_idx])):
                # the position can place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = True, True, True
                stack.append((rdx + 1, cols[:], lefts[:], rights[:],
                              positions + [(rdx, cdx)]))
                # the position does not place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = False, False, False
    return ans


def queens_with_a_fixed_position(x, y, n_queen=8):
    """
    uva 750
    backtracking, searching by row first then by column.
    the size of the board is n_row * n_col (rdx from 0 to n_row -1 (n_col - 1)
    if there is a queen placed in board[rdx][cdx], then
        the rdx row, the cdx column, the diagonal (rdx+cdx)%(2*(n_col)-1), and
        the diagonal ((rdx-cdx)+(2*(n_col)-1))%((2*(n_col)-1) can't place
        another queen.

    x, y is the location of a given queen.
    """
    # square chessboard
    n_row = n_col = n_queen
    d_size = (2 * n_col - 1)
    ans = []

    # initial condition
    i_cols = [False] * n_col
    i_cols[y] = True
    i_lefts, i_rights = [False] * d_size, [False] * d_size
    i_lefts[(x + y) % d_size], i_rights[(x - y) % d_size] = True, True

    # (rdx, cols, left_diagonal, right_diagonal, positions)
    stack = [(0, i_cols, i_lefts, i_rights, [(x, y)])]

    while stack:
        rdx, cols, lefts, rights, positions = stack.pop()
        # print (rdx, cols, positions)
        if rdx >= n_row:
            # because the xth row will not be checked, there are only
            # n_row -1 rows need to be checked
            if len(positions) == n_queen:
                ans.append(positions)
            continue

        if rdx == x:
            stack.append((rdx + 1, cols[:], lefts[:], rights[:],
                          positions[:]))
            continue

        for cdx in range(n_col):
            l_idx, r_idx = (rdx + cdx) % d_size, (rdx - cdx) % d_size
            if not any((cols[cdx], lefts[l_idx], rights[r_idx])):
                # the position can place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = True, True, True
                stack.append((rdx + 1, cols[:], lefts[:], rights[:],
                              positions + [(rdx, cdx)]))
                # the position does not place a new queen
                cols[cdx], lefts[l_idx], rights[r_idx] = False, False, False
    return ans


def test_queens():
    for idx in range(10):
        assert queens(idx) == queens_iterative(idx)


def Kruskal_mst(locs, n_node):
    """
    uva 10034
    full connected graph, and the locs are the coordinates the each node.
    Kruskal's algorithm
    """
    import math
    lsqrt = math.sqrt
    graph = {}
    for idx in range(n_node):
        x1, y1 = locs[idx]
        for jdx in range(idx + 1, n_node):
            x2, y2 = locs[jdx]
            dx, dy = (x1 - x2), (y1 - y2)
            graph[(idx, jdx)] = lsqrt(dx * dx + dy * dy)
    graph = sorted(graph.items(), key=lambda x: x[1])

    # store the id in which set
    sets = list(range(n_node))
    # store the set contains what ids
    groups = [[idx] for idx in range(n_node)]
    n_edge, costs = 0, 0
    for gdx, ((n1, n2), d) in enumerate(graph):
        if sets[n1] != sets[n2]:
            costs += d
            n_edge += 1
            # union set, merge small set to large one
            if len(groups[sets[n1]]) > len(groups[sets[n2]]):
                groups[sets[n1]].extend(groups[sets[n2]])
                tmp = sets[n2]
                for idx in groups[sets[n2]]:
                    sets[idx] = sets[n1]
                groups[tmp].clear()

            else:
                groups[sets[n2]].extend(groups[sets[n1]])
                tmp = sets[n1]
                for idx in groups[sets[n1]]:
                    sets[idx] = sets[n2]
                groups[tmp].clear()

        if n_edge == n_node - 1:
            break

    return costs


def articulation_points(graph, n_node, roots=[0, ]):
    """
    uva 315, the graph may be disconnected.
    graph: edge list
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
            visited[node] = step
            lows[node] = step
            step += 1
            components[node] = com_id
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

    return articulations

def arbitrage(graph, n_node):
    """
    uva 104
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

                    if wealth[kdx][idx][jdx] > 1.01 and idx == jdx:
                        stack = [(kdx, path[kdx][idx][idx])]
                        ans = [idx, ]
                        while stack:
                            step, prev_node = stack.pop()
                            if prev_node != -1:
                                ans.append(prev_node)
                                stack.append(
                                    (step - 1, path[step - 1][idx][prev_node]))
                        ans.append(idx)
                        return " ".join(str(v + 1) for v in reversed(ans))

        # # if we check the results after all exchange in kth loop,
        # # then results will be the same as given.
        # for idx in range(n_node):
        #     if wealth[kdx][idx][idx] > 1.01:
        #         return path_traceback(path, kdx, idx)

    # no arbitrage
    return "no arbitrage sequence exists"


def topological_sort(graph, n_node):
    """ uva 10305, 200, graph: edge list """

    orders = []
    candidate_roots = set(range(n_node))

    # the worst case requires checking all nodes once
    for _ in range(n_node):
        node_have_in_edges = set()
        for node in candidate_roots:
            for e in graph[node]:
                if e in candidate_roots:
                    node_have_in_edges.add(e)
        roots = list(candidate_roots - node_have_in_edges)
        candidate_roots = node_have_in_edges
        orders.extend(roots)
        if len(orders) >= n_node:
            break

    if len(orders) < n_node:
        raise ValueError('there is a cycle in the graph.')

    return " ".join(str(v + 1) for v in orders)


def Dijkstra_queue(graph, n_node, src, tgt):
    """
    uva 10986
    Dijkstra algorithm implemented using the priority queue
    """
    import heapq
    INF = 2 << 31
    visited = [False] * n_node
    # store the distance from src to all other nodes
    dist = [INF] * n_node
    dist[src] = 0
    # (dist, node), the queue will adjust by dist.
    queue = [(0, src), ]
    q_push, q_pop = heapq.heappush, heapq.heappop

    while queue:
        # always the node with the smallest distance
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
