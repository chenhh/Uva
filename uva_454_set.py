# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/454.pdf

don't strip in the input, otherwise it gets PE.
"""


def solve(phases):
    counts = [(phase, "".join(sorted("".join(phase.split()))))
              for phase in phases]
    # brute force
    sorted_counts = sorted(counts, key=lambda x: x[0])
    length = len(sorted_counts)
    for idx, (k1, p1) in enumerate(sorted_counts):
        for jdx in range(idx + 1, length):
            k2, p2 = sorted_counts[jdx]
            if p1 == p2:
                print("{} = {}".format(k1, k2))


def main():
    n_case = int(input())
    _ = input()
    phases = []
    append = phases.append

    for tdx in range(n_case):
        phases.clear()
        while 1:
            try:
                phase = input()
                if phase:
                    append(phase)
                else:
                    break
            except (EOFError):
                break
        solve(phases)
        if tdx != n_case - 1:
            print()


if __name__ == '__main__':
    main()
