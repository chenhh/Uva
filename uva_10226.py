# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/102/10226.pdf
both using dict or list with bisect will be TLE
"""

def bisect_count(forest, tree):
    """
    bisect right
    """
    lo, hi =0, len(forest)
    while lo < hi:
        mid = (lo + hi) // 2
        if tree < forest[mid][0]:
            hi = mid
        else:
            lo = mid + 1
    # print ("insert point:", lo)

    if lo == 0:
        # no element in forest
        forest.insert(0, [tree, 1])
    elif forest[lo-1][0] == tree:
        # the tree exists in forest
        forest[lo-1][1] += 1
    else:
        # the tree not in forest
        forest.insert(lo, [tree, 1])

    return forest

def main():
    cases = int(input())
    _ = input()

    for cdx in range(cases):
        species = []
        tree_cnt = 0

        while 1:
            tree = input().strip()
            if len(tree) == 0:
                break
            tree_cnt += 1
            bisect_count(species, tree)

        for tree, cnt in species:
            percent = cnt/tree_cnt * 100
            print("{} {:.4f}".format(tree, percent))

        if cdx != cases-1:
            # blank line between consecutive cases
            print("")

if __name__ == '__main__':
    main()
