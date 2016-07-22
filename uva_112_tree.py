# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/112.pdf
http://luckycat.kshs.kh.edu.tw/homework/q112.htm

- there are negative values in the tree.
- to determine a node in the tree is a leaf node.
- binary tree
"""

import sys
from collections import deque


def main():
    recs = iter(sys.stdin.read())
    tree = deque()
    tree_append = tree.append
    tree_pop = tree.pop
    tree_clear = tree.clear

    num = deque()
    num_append = num.append
    num_clear = num.clear

    while True:
        try:
            # read query number
            while not tree:
                ch = next(recs)
                if ch in '-0123456789':
                    num_append(ch)
                elif ch == '(':
                    query = int("".join(num))
                    num_clear()

                    # initialize
                    tree_append(ch)
                    path = []
                    n_left_brace = 1
                    is_match = False
                    break

            # read tree
            ch = next(recs)

            if ch in ' \n':
                # skip space and newline
                continue

            elif ch == '(':
                # next sub-tree
                tree_append(ch)
                n_left_brace += 1

            elif ch == ')':
                if tree[-1] == '(':
                    # an empty node, use none to represent it
                    tree_pop()
                    tree_append(None)
                else:
                    none_cnt = 0
                    while tree[-1] != '(':
                        val = tree_pop()
                        if val is None:
                            # cnt the empty sub-nodes in the current node
                            none_cnt += 1
                        if isinstance(val, int):
                            if none_cnt == 2:
                                # an leaf node
                                # print (path, sum(path), query,
                                #        sum(path) == query)
                                if sum(path) == query:
                                    is_match = True
                            path.pop()

                    # pop the left brace
                    tree_pop()
                n_left_brace -= 1

            elif ch in '-0123456789':
                num_append(ch)
                while True:
                    v = next(recs)
                    if v in '-0123456789':
                        num_append(v)
                    else:
                        value = int("".join(num))
                        path.append(value)
                        tree_append(sum(path))

                        num_clear()
                        if v == '(':
                            # after a value, it must be a left brace.
                            tree_append(v)
                            n_left_brace += 1
                        # elif v == ')':
                        #     # illegal value
                        #     tree_append(v)
                        #     n_left_brace -= 1
                        break

            if not n_left_brace:
                # end of a tree
                if is_match:
                    print("yes")
                else:
                    print("no")
                tree_clear()

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
