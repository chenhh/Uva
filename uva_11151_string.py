# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/111/11151.pdf

palidrome[sdx][edx] =
    2 + longest[sdx+1][edx-1] ,                    if word[sdx] == word[edx]
    max(longest[sdx][edx-1], longest[sdx+1][edx]), otherwise

"""

import sys


def longest_palindrome(word, sdx, edx, table):
    """ uva 11151 """
    if sdx == edx:
        # the empty string is a palindrome
        return 1

    if sdx == edx - 1:
        if word[sdx] == word[edx]:
            return 2
        else:
            return 1

    if table[sdx][edx] != -1:
        # checked
        return table[sdx][edx]

    if word[sdx] == word[edx]:
        table[sdx][edx] = 2 + longest_palindrome(word, sdx + 1, edx - 1, table)
    else:
        table[sdx][edx] = max(longest_palindrome(word, sdx, edx - 1, table),
                              longest_palindrome(word, sdx + 1, edx, table))
    return table[sdx][edx]


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        word = next(recs).strip()
        len_word = len(word)
        if len_word == 0:
            print(0)
        else:
            table = [[-1] * len_word for _ in range(len_word)]
            print(longest_palindrome(word, 0, len_word - 1, table))


if __name__ == '__main__':
    main()
