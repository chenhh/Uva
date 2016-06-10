# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/102/10293.pdf
"""

from collections import deque


def main():
    lines, words = [], []
    while 1:
        try:
            data = input().strip()
            if data != '#':
                lines.append(data)
            else:
                lines.append('@')
                article = "@".join(lines).lower()
                article = article.replace('-@', '')
                # print (article)
                # Words can be separated by blanks, question marks,
                # exclaimation marks, commas and periods
                words_cnt, chars = [0] * 30, deque()
                for c in article:
                    if c not in (' ', '?', '!', ',', '.', '@'):
                        if c not in ("'", '-'):
                            chars.append(c)
                    else:
                        word = "".join(chars)
                        if len(word):
                            # print (word, len(word))
                            words_cnt[len(word) - 1] += 1
                        chars.clear()

                for idx, cnt in enumerate(words_cnt):
                    if cnt:
                        print(idx + 1, cnt)
                print()
                words.clear()
                lines.clear()

        except (EOFError):
            break


if __name__ == '__main__':
    main()
