# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

http://luckycat.kshs.kh.edu.tw/homework/q548.htm
https://uva.onlinejudge.org/external/5/548.pdf

binary tree
"""


def post_in_order_to_tree(post_nodes, in_nodes):
    """
    dict to implement a binary tree,
    nodes: list of values
    """
    tree = {}
    stack = []
    stack.append((post_nodes, in_nodes, tree))
    while len(stack):
        sub_post_nodes, sub_in_nodes, sub_tree = stack.pop()
        root = sub_post_nodes[-1]
        sub_tree['value'] = root

        if len(sub_post_nodes) == 1:
            # leaf node
            sub_tree['lchild'] = sub_tree['rchild'] = None
        else:
            # internal node
            # distinguish left and right sub_trees in infix nodes
            left_in_count = 0
            for node in sub_in_nodes:
                if node == root:
                    break
                left_in_count += 1

            # left sub_tree
            if left_in_count:
                sub_post_left_nodes = sub_post_nodes[:left_in_count]
                sub_in_left_nodes = sub_in_nodes[:left_in_count]
                sub_tree['lchild'] = {}
                stack.append((sub_post_left_nodes, sub_in_left_nodes,
                              sub_tree['lchild']))
            else:
                sub_tree['lchild'] = None

            # right sub_tree
            right_in_count = len(sub_in_nodes) - left_in_count - 1
            if right_in_count:
                sub_post_right_nodes = sub_post_nodes[left_in_count:-1]
                sub_in_right_nodes = sub_in_nodes[left_in_count + 1:]
                sub_tree['rchild'] = {}
                stack.append((sub_post_right_nodes, sub_in_right_nodes,
                              sub_tree['rchild']))
            else:
                sub_tree['rchild'] = None

    return tree


def all_tree_paths(tree, output=[], paths=[]):
    if tree:
        output.append(tree['value'])
        if tree['lchild']:
            all_tree_paths(tree['lchild'], output, paths)
        if tree['rchild']:
            all_tree_paths(tree['rchild'], output, paths)
        elif not tree['lchild'] and not tree['rchild']:
            paths.append(output[:])
        output.pop()
    return paths


def main():
    while 1:
        try:
            in_nodes = list(map(int, input().split()))
            post_nodes = list(map(int, input().split()))
            tree = post_in_order_to_tree(post_nodes, in_nodes)
            paths = all_tree_paths(tree, [], [])

            min_cost, min_path_node = 1e10, None
            for idx, path in enumerate(paths):
                cost = sum(path)
                if cost < min_cost:
                    min_cost = cost
                    min_path_node = path[-1]
                if cost == min_cost and path[-1] < min_path_node:
                    min_path_node = path[-1]
            print(min_path_node)
        except (EOFError):
            break


if __name__ == '__main__':
    main()
