# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/107/10701.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10701.htm
"""


def pre_in_order_to_tree(pre_nodes, in_nodes):
    """
    dict to implement a binary tree,
    nodes: list of values
    """
    tree = {}
    stack = []
    stack.append((pre_nodes, in_nodes, tree))
    while len(stack):
        sub_pre_nodes, sub_in_nodes, sub_tree = stack.pop()
        root = sub_pre_nodes[0]
        sub_tree['value'] = root

        if len(sub_pre_nodes) == 1:
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
                sub_pre_left_nodes = sub_pre_nodes[1:1 + left_in_count]
                sub_in_left_nodes = sub_in_nodes[:left_in_count]
                sub_tree['lchild'] = {}
                stack.append((sub_pre_left_nodes, sub_in_left_nodes,
                              sub_tree['lchild']))
            else:
                sub_tree['lchild'] = None

            # right sub_tree
            right_in_count = len(sub_in_nodes) - left_in_count - 1
            if right_in_count:
                sub_pre_right_nodes = sub_pre_nodes[1 + left_in_count:]
                sub_in_right_nodes = sub_in_nodes[left_in_count + 1:]
                sub_tree['rchild'] = {}
                stack.append((sub_pre_right_nodes, sub_in_right_nodes,
                              sub_tree['rchild']))
            else:
                sub_tree['rchild'] = None

    return tree


def post_order(tree, output=[]):
    """ left -> right -> value """
    if not tree:
        return
    post_order(tree['lchild'], output)
    post_order(tree['rchild'], output)
    output.append(tree['value'])
    return output


def main():
    C = int(input())
    for _ in range(C):
        n_node, pre_nodes, in_nodes = input().split()
        tree = pre_in_order_to_tree(pre_nodes, in_nodes)
        output = post_order(tree, [])
        print("".join(output))


if __name__ == '__main__':
    main()
