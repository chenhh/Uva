# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/101/10100.pdf

longest common sub-sequence of words.
Note: the word is case-sensitive.
"""

import sys


def lcs(line1, line2):
    """
    line1: list of words, the first word is empty.
    line2: list of words, the first word is empty.
    """
    len1 = len(line1)
    len2 = len(line2)
    # n_row: len2, n_col: len1
    length = [[0] * len2 for _ in range(len1)]
    for idx in range(1, len1):
        for jdx in range(1, len2):
            if line1[idx] == line2[jdx]:
                length[idx][jdx] = length[idx - 1][jdx - 1] + 1
            else:
                length[idx][jdx] = max(length[idx - 1][jdx],
                                       length[idx][jdx - 1])
    return length[len1 - 1][len2 - 1]


def parse(data):
    """ a word contains only alphabet """
    if not data:
        return None

    words = ["", ]
    stack = []
    for c in data:
        if c.isalnum():
            stack.append(c)
        else:
            if stack:
                words.append("".join(stack))
                stack.clear()
    if stack:
        words.append("".join(stack))
        stack.clear()

    return words


def main():
    recs = iter(sys.stdin.readlines())
    case = 0
    while True:
        try:
            case += 1
            line1 = parse(next(recs).strip())
            line2 = parse(next(recs).strip())
            if line1 is None or line2 is None:
                print("{:>2d}. Blank!".format(case))
                continue

            length = lcs(line1, line2)
            print("{:>2d}. Length of longest match: {}".format(case, length))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
