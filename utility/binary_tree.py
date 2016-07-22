# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

def pre_order_to_binary_search_tree(nodes):
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


def pre_in_order_to_binary_tree(pre_nodes, in_nodes):
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
            # print (left_in_count,
            #        "infix left:", sub_in_nodes[:left_in_count],
            #        " right:", sub_in_nodes[left_in_count+1:])
            # print ("prefix left:", sub_pre_nodes[1:1 + left_in_count],
            #         "right:",sub_pre_nodes[1 + left_in_count:])

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
                sub_in_right_nodes = sub_in_nodes[left_in_count+1:]
                sub_tree['rchild'] = {}
                stack.append((sub_pre_right_nodes, sub_in_right_nodes,
                              sub_tree['rchild']))
            else:
                sub_tree['rchild'] = None

    return tree


def post_in_order_to_binary_tree(post_nodes, in_nodes):
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


def pre_order(tree, output=[]):
    """ value -> left -> right """
    if not tree:
        return
    output.append(tree['value'])
    pre_order(tree['lchild'], output)
    pre_order(tree['rchild'], output)
    return output


def pre_order_stack(tree):
    if not tree:
        return

    stack = [tree, ]
    while stack:
        node = stack.pop()
        print(node['value'])

        if node['lchild']:
            stack.append(node['lchild'])
        if node['rchild']:
            stack.append(node['rchild'])



def post_order(tree, output=[]):
    """ left -> right -> value """
    if not tree:
        return
    post_order(tree['lchild'], output)
    post_order(tree['rchild'], output)
    output.append(tree['value'])
    return output


def greedy_min_cost_traversal(tree):
    """
    on each branch of the tree, always choose the node with smaller value.
    """
    # greedy find the path with smaller values in each branch first
    if not tree:
        return 0

    greedy_cost = 0
    greedy_path = []
    sub_tree = tree
    while sub_tree:
        greedy_cost += sub_tree['value']
        greedy_path.append(sub_tree['value'])
        if sub_tree['lchild'] and sub_tree['rchild']:
            # both sub_trees exist
            if sub_tree['lchild']['value'] < sub_tree['rchild']['value']:
                sub_tree = sub_tree['lchild']
            else:
                sub_tree = sub_tree['rchild']
        elif not sub_tree['rchild']:
            # only left sub_tree exists
            sub_tree = sub_tree['lchild']
        elif not sub_tree['lchild']:
            # only right sub_tree exists
            sub_tree = sub_tree['rchild']

    return greedy_cost, greedy_path

def all_binary_tree_paths(tree, output=[], paths=[]):
    """
    traversal all paths in a tree
    return list of all paths (a path is the nodes from root to leaf)
    """

    if tree:
        output.append(tree['value'])
        if tree['lchild']:
            all_binary_tree_paths(tree['lchild'], output, paths)
        if tree['rchild']:
            all_binary_tree_paths(tree['rchild'], output, paths)
        elif not tree['lchild'] and not tree['rchild']:
            paths.append(output[:])
        output.pop()
    return paths