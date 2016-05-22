# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/123/12347.pdf

binary search tree, max nodes: 10000
given pre-order, to get post-order
the first element is the root node, and the nodes which are smaller than
the root node are in the left-subtree, other nodes are in the right-subtree.
"""


def pre_order_to_tree(nodes):
    """
    dict to implement binary tree,
    nodes: list of values
    """
    stack = []
    tree = {}
    stack.append((nodes, tree))

    while len(stack):
        sub_nodes, sub_tree = stack.pop()
        root = sub_nodes[0]
        sub_tree['value'] = root

        if len(sub_nodes) == 1:
            # leaf node
            sub_tree['lchild'] = sub_tree['rchild'] = None
        else:
            # internal node
            smaller = 0
            for node in sub_nodes[1:]:
                if node > root:
                    break
                smaller += 1

            # check left sub-tree
            if smaller:
                left_children = sub_nodes[1:1 + smaller]
                sub_tree['lchild'] = {}
                stack.append((left_children, sub_tree['lchild']))
            else:
                sub_tree['lchild'] = None

            # check right sub-tree
            larger = len(sub_nodes) - smaller - 1
            if larger:
                right_children = sub_nodes[1 + smaller:]
                sub_tree['rchild'] = {}
                stack.append((right_children, sub_tree['rchild']))
            else:
                sub_tree['rchild'] = None

    return tree


def pre_order(tree, output=[]):
    """ value -> left -> right """
    if not tree:
        return
    output.append(tree['value'])
    pre_order(tree['lchild'])
    pre_order(tree['rchild'])
    return output


def post_order(tree, output=[]):
    """ left -> right -> value """
    if not tree:
        return
    post_order(tree['lchild'])
    post_order(tree['rchild'])
    output.append(tree['value'])
    return output


def main():
    nodes = []
    while 1:
        try:
            # pre-order
            node = int(input())
            nodes.append(node)
        except (EOFError):
            tree = pre_order_to_tree(nodes)
            outputs = post_order(tree)
            for val in outputs:
                print(val)
            break


def test():
    import pprint
    pre_order_list = [50, 30, 24, 5, 28, 45, 98, 52, 60]
    tree = pre_order_to_tree(pre_order_list)
    pre_order_list2 = pre_order(tree)
    pprint.pprint(tree)
    assert pre_order_list == pre_order_list2


if __name__ == '__main__':
    main()
