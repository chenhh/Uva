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
import pprint

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


def post_order(tree):
    """ left-> right-> value """
    stack = [tree, ]
    output = []
    while len(stack):
        node = stack.pop()
        pprint.pprint(node)
        print ('-'*60)
        # left sub_tree
        if node['lchild']:
            stack.append(node['lchild'])

        # right sub_tree
        if node['rchild']:
            stack.append(node['rchild'])

        if not node['lchild'] and not node['rchild']:
            output.append(node['value'])

    print(output)
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
            print(post_order(tree))



if __name__ == '__main__':
    # main()
    # print (pre_order_to_tree([10,2,1,12]))
    import pprint
    # tree = pre_order_to_tree([4, 2, 1, 3, 5, 0])
    tree = pre_order_to_tree([50, 30, 24, 5, 28, 45, 98, 52, 60])
    # pprint.pprint(tree)
    output = post_order(tree)
    print(output)
