# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/5/531.pdf
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

    lcs_length = length[len1 - 1][len2 - 1]

    # traceback
    idx = len1 - 1
    jdx = len2 - 1
    lcs_words = [[] for _ in range(lcs_length)]
    kdx = lcs_length - 1
    while kdx >= 0:
        if line1[idx] == line2[jdx]:
            # match
            lcs_words[kdx] = line1[idx]
            kdx -= 1
            idx -= 1
            jdx -= 1
        else:
            if length[idx][jdx - 1] > length[idx - 1][jdx]:
                # the lcs values comes from left
                jdx -= 1
            else:
                # the lcs values comes from upper
                idx -= 1

    return lcs_length, lcs_words


def main():
    recs = iter(sys.stdin.readlines())

    text1 = []
    text2 = []
    case = 0
    while True:
        try:
            data = next(recs).split()
            if data[0] == '#':
                case = (case + 1) % 2

                if case == 0:
                    # inserting empty string for lcs
                    text1.insert(0, "")
                    text2.insert(0, "")
                    length, words = lcs(text1, text2)
                    print(" ".join(words))
                    text1.clear()
                    text2.clear()
                continue

            if case == 0:
                text1.extend(data)
            else:
                text2.extend(data)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
