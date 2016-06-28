# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10935.pdf
"""

import sys
from collections import deque


def main():
    # cache the answer
    discards_list, remain_list = [], []
    for n_card in range(1, 51):
        discards = []
        remains = deque(str(v + 1) for v in range(n_card))
        while len(remains) > 1:
            discards.append(remains.popleft())
            top = remains.popleft()
            remains.append(top)
        discards_list.append(discards)
        remain_list.append(remains[0])

    recs = sys.stdin.readlines()

    for rec in recs:
        n = int(rec)
        if not n:
            break

        print("Discarded cards: {}".format(
            ", ".join(discards_list[n - 1])).strip())
        print("Remaining card: {}".format(remain_list[n - 1]))


if __name__ == '__main__':
    main()
