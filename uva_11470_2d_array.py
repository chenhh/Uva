# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/114/11470.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    case = 0

    while True:
        n_size = int(next(recs))
        if not n_size:
            break
        squares = [list(map(int, next(recs).split())) for _ in range(n_size)]

        values = []
        n_level, rem = divmod(n_size, 2)
        if rem:
            n_level += 1

        for level in range(0, n_level):
            value = 0
            upper_bound = n_size - level - 1
            for idx in range(level, upper_bound + 1):
                if idx in (level, upper_bound):
                    for jdx in range(level, upper_bound + 1):
                        # print(idx, jdx)
                        value += squares[idx][jdx]
                else:
                    for jdx in (level, upper_bound):
                        # print (idx, jdx)
                        value += squares[idx][jdx]
            # print ()
            values.append(value)
        case += 1
        print("Case {}: {}".format(case, " ".join(str(v) for v in values)))


if __name__ == '__main__':
    main()
