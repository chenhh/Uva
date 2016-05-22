# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
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
            # print ("sub_nodes:", sub_nodes, root)
            # print ("slice:", smaller, sub_nodes[1:1+smaller],
            #        sub_nodes[1 + smaller:])
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