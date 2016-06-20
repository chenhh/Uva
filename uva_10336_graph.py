# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/103/10336.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10336.htm
"""

import sys

# N, E, S, W
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


def connected_components(region, n_row, n_col):
    global directiions
    lang_cnt = {region[0][0]: 1}
    lang_get = lang_cnt.get

    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        if 'a' <= region[x][y] <= 'z':
            lang = region[x][y]
            region[x][y] = region[x][y].upper()
            for h, v in directions:
                if (0 <= x + h <= n_row - 1 and 0 <= y + v <= n_col - 1 and
                            region[x + h][y + v] == lang):
                    stack.append((x + h, y + v))

        # find next region
        if not stack:
            for rdx, row in enumerate(region):
                if stack:
                    break
                for cdx, c in enumerate(row):
                    if 'a' <= c <= 'z':
                        stack.append((rdx, cdx))
                        lang_cnt[region[rdx][cdx]] = (
                            lang_get(region[rdx][cdx], 0) + 1)
                        break

    return lang_cnt


def main():
    recs = iter(sys.stdin.readlines())

    n_case = int(next(recs))
    for tdx in range(n_case):
        n_row, n_col = list(map(int, next(recs).split()))
        if n_row == 0:
            print("World #{}".format(tdx + 1))
            continue
        region = [list(next(recs).strip()) for _ in range(n_row)]
        lang_dict = connected_components(region, n_row, n_col)
        lang_cnt = sorted(lang_dict.items(), key=lambda x: (-x[1], x[0]))
        print("World #{}".format(tdx + 1))
        # sort by count, then by lexical order
        for k, v in lang_cnt:
            print("{}: {}".format(k, v))


if __name__ == '__main__':
    main()
