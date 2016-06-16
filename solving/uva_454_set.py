# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/454.pdf
"""

import sys


def solve(phases):
    counts = {phase: "".join(sorted("".join(phase.split())))
              for phase in phases}
    # brute force
    sorted_keys = sorted(counts.keys())
    len_keys = len(sorted_keys)
    for idx in range(len_keys):
        k1 = sorted_keys[idx]
        for jdx in range(idx + 1, len_keys):
            k2 = sorted_keys[jdx]
            if counts[k1] == counts[k2]:
                print("{} = {}".format(k1, k2))


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)
    phases = []
    append = phases.append
    case = 0
    while 1:
        try:
            phase = next(recs).strip()
            if phase:
                append(phase)
            else:
                solve(phases)
                case += 1
                if case != n_case - 1:
                    print()
                phases.clear()

        except StopIteration:
            if phases:
                solve(phases)
            break


if __name__ == '__main__':
    main()
