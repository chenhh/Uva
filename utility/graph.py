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


def connected_components(graph, n_node):
    """ uva 572, dfs search """
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
