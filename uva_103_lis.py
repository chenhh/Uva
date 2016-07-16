# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/103.pdf
http://luckycat.kshs.kh.edu.tw/homework/q103.htm

longest increasing sequence
"""

import sys


def cmp_dominated(box_item1, box_item2):
    """
    box_item: key, values

    return a negative value for less-than,
    return zero if they are equal, or
    return a positive value for greater-than.
    """
    _, box1 = box_item1
    _, box2 = box_item2
    n_dim = len(box1)

    for idx in range(n_dim):
        if box1[idx] >= box2[idx]:
            # box2 does not dominating box1, equal
            return 0
    # box2 dominating box1
    return 1


def dp_lis(box_items, n_box):
    """
    dynamic programming
    lis(n) = max (lis(i) + 1: if s[i] <s[n])
    """
    keys, boxes = zip(*box_items)

    # each element is an lis of length 1
    len_lis = [1] * n_box
    prev = [-1] * n_box

    for idx in range(n_box):
        for jdx in range(idx + 1, n_box):
            if cmp_dominated(box_items[idx], box_items[jdx]):
                # jdx dominating idx
                if len_lis[idx] + 1 > len_lis[jdx]:
                    # jdx item is behind the idx item
                    len_lis[jdx] = len_lis[idx] + 1
                    prev[jdx] = idx
    # print (len_lis)
    # print (prev)
    max_len_lis = max(len_lis)

    # traceback
    curr = 0
    for idx in range(n_box):
        if len_lis[idx] == max_len_lis:
            curr = idx
            break

    ans = []
    while curr != -1:
        ans.append(keys[curr])
        curr = prev[curr]

    return (max_len_lis, " ".join(map(str, ans[::-1])))


def main():
    recs = iter(sys.stdin.readlines())

    while True:
        try:
            n_box, n_dim = list(map(int, next(recs).split()))

            box_items = [(idx + 1, sorted(list(map(int, next(recs).split()))))
                         for idx in range(n_box)]
            # lis comparison
            box_items.sort(key=lambda x: x[1])

            length, ans = dp_lis(box_items, n_box)
            print(length)
            print(ans)


        except (StopIteration):
            break


if __name__ == '__main__':
    main()
