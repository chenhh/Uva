# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/3/324.pdf
"""

import sys


def main():
    facts = [1, ]
    for v in range(2, 367):
        facts.append(facts[-1] * v)
    digits = {}
    for idx, val in enumerate(facts):
        digits[idx + 1] = [0] * 10
        for d in str(val):
            digits[idx + 1][int(d)] += 1

    recs = sys.stdin.readlines()
    for rec in recs:
        val = int(rec)
        if not val:
            break
        print("{}! --".format(val))

        for idx in range(5):
            if idx:
                print("    ", end="")
            else:
                print("   ", end="")
            print("({}){:>5}".format(idx, digits[val][idx]), end="")
        print()
        for idx in range(5, 10):
            if idx != 5:
                print("    ", end="")
            else:
                print("   ", end="")
            print("({}){:>5}".format(idx, digits[val][idx]), end="")
        print()


if __name__ == '__main__':
    main()
