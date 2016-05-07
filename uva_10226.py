# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: on judge
difficulty: 1

https://uva.onlinejudge.org/external/102/10226.pdf
"""
import bisect


def main():
    cases = int(input())

    case_cnt = 0
    species = []
    while True:
        try:
            tree = input().strip()

            if len(tree) > 0:
                bisect.insort_right(species, tree)
            else:
                if case_cnt >= 1 and case_cnt <= cases:
                    n_tree = len(species)
                    if n_tree == 0:
                        print ("")
                    else:
                        sdx = 0
                        # print ("{} {}: {}".format(case_cnt, n_tree, species))
                        for tdx, tree in enumerate(species):
                            if ((tdx >=1 and species[tdx-1] != tree)):
                                # print (tdx, sdx)
                                percent = (tdx-sdx)/n_tree * 100
                                print ("{} {:.4f}".format(
                                    species[sdx], percent ))
                                sdx = tdx
                        # print last set
                        percent = (n_tree-sdx)/n_tree * 100
                        print("{} {:.4f}".format(species[sdx], percent))

                    if case_cnt != cases:
                        print("")

                case_cnt += 1
                species = []

            if case_cnt > cases:
                break
        except (EOFError):
            break

if __name__ == '__main__':
    main()
