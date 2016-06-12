# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/3/353.pdf
"""

import sys


def palindrome(word):
    return all(word[idx] == word[len(word) - idx - 1]
               for idx in range(len(word) // 2))


def main():
    records = sys.stdin.readlines()
    # substrings = set()

    for rec in records:
        word = rec.strip()
        substrings = set(word[sdx:edx]
                         for sdx in range(len(word))
                         for edx in range(sdx + 1, len(word) + 1)
                         if palindrome(word[sdx:edx]))
        print("The string '{}' contains {} palindromes.".format(
            word, len(substrings)))


if __name__ == '__main__':
    main()
