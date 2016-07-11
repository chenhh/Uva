# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/6/624.pdf
"""

import sys
from itertools import compress


def cd(minutes, n_track, tracks):
    chosen_set = set()
    # (sum of minutes, curr_track, chosen),
    stack = [(0, 0, [False] * n_track), ]
    stack_append = stack.append
    stack_pop = stack.pop
    min_diff = minutes
    max_n_chosen = 0
    min_chosen = None
    while stack:
        chosen_min, curr, chosen = stack_pop()

        diff = minutes - chosen_min
        # the '=' will fit the longest match
        if min_diff >= diff:
            min_diff = diff
            min_chosen = chosen[:]

        if curr >= n_track:
            continue

        curr_min = chosen_min + tracks[curr]
        if curr_min <= minutes:
            # choose curr song
            chosen[curr] = True
            stack_append((curr_min, curr + 1, chosen[:]))
            chosen[curr] = False
        # not chose curr song
        stack_append((chosen_min, curr + 1, chosen[:]))

    data = " ".join(str(v) for v in compress(tracks, min_chosen))
    return "{} sum:{}".format(data, minutes - min_diff)


def main():
    recs = sys.stdin.readlines()
    for rec in recs:
        vals = list(map(int, rec.split()))
        minutes = vals[0]
        n_track = vals[1]
        tracks = vals[2:]
        print(cd(minutes, n_track, tracks))


if __name__ == '__main__':
    main()
