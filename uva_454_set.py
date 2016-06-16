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
    counts = {phase: "".join(sorted(phase.split())) for phase in phases}
    for key in sorted(counts.key()):
        chars1 = counts[key]


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
                if case:
                    print()
                solve(phases)
                case += 1
                phases.clear()

        except StopIteration:
            if phases:
                if case:
                    print()
                solve(phases)
                case += 1


if __name__ == '__main__':
    main()
