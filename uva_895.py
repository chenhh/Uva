# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/8/895.pdf
"""

from collections import Counter


def main():
    words = []
    while 1:
        word = input().strip()
        if word == '#':
            break
        words.append(Counter(word))

    while 1:
        chars = input().split()
        if chars[0] == '#':
            break
        chars = Counter(chars)
        count = 0
        for word in words:
            ok = True
            for c in word:
                if word[c] > chars[c]:
                    ok = False
                    break
            if ok:
                count += 1
        print(count)


if __name__ == '__main__':
    main()
