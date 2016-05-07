# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/102/10226.pdf
both using dict or list with bisect will be TLE
"""
import bisect

def main():
    cases = int(input())
    _ = input()

    for cdx in range(cases):
        # species_name = []
        species_cnt ={}
        tree_cnt = 0

        while True:
            tree = input().strip()
            if len(tree) == 0:
                break

            if tree in species_cnt:
                species_cnt[tree] += 1
            else:
                # bisect.insort_right(species_name, tree)
                species_cnt[tree] = 1
            tree_cnt += 1

        keys = sorted(species_cnt.keys())
        for key in keys:
            percent = species_cnt[key]/tree_cnt * 100
            print("{} {:.4f}".format(key, percent))

        if cdx != cases-1:
            # blank line between consecutive cases
            print("")

if __name__ == '__main__':
    main()
