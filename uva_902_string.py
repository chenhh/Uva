# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/9/902.pdf
"""

from collections import Counter


def main():
    while 1:
        try:
            # the input may not in a line
            data = input().split()
            if len(data) < 2:
                n = int(data[0])
                cipher = input().split()[0]
            else:
                n, cipher = int(data[0]), data[1]

            words = Counter(cipher[idx: idx + n]
                            for idx in range(len(cipher) - n + 1))
            # assuming there is a unique most frequency substring
            print(words.most_common(1)[0][0])

        except (EOFError):
            break


if __name__ == '__main__':
    main()
