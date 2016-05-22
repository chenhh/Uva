# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

http://luckycat.kshs.kh.edu.tw/homework/q548.htm
https://uva.onlinejudge.org/external/5/548.pdf
prune search
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
                sub_in_right_nodes = sub_in_nodes[left_in_count+1:]
                sub_tree['rchild'] = {}
                stack.append((sub_post_right_nodes, sub_in_right_nodes,
                              sub_tree['rchild']))
            else:
                sub_tree['rchild'] = None

    return tree

def min_cost_traversal(tree):
    """
    the cost of a path is sum of nodes in the path.
    return the terminal node with in the min cost path.
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

def main():
    import pprint
    while 1:
        try:
            in_nodes = list(map(int, input().split()))
            post_nodes = list(map(int, input().split()))
            tree = post_in_order_to_tree(post_nodes, in_nodes)
            # pprint.pprint(tree)
            print (min_cost_traversal(tree))
        except (EOFError):
            break

if __name__ == '__main__':
    main()
    # import pprint
    # tree = post_in_order_to_tree('3125674', '3214576')
    # pprint.pprint(tree)
    # print(min_cost_traversal(tree, [], 0))
