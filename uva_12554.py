# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12554.pdf
"""


def main():
    songs = ['Happy', 'birthday', 'to', 'you',
             'Happy', 'birthday', 'to', 'you',
             'Happy', 'birthday', 'to', 'Rujia',
             'Happy', 'birthday', 'to', 'you']

    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())

    len_s, len_n = len(songs), len(names)

    if len_s >= len_n:
        # name repeat
        for idx in range(len_s):
            print("{}: {}".format(names[idx % len_n], songs[idx]))

    else:
        # song repeat
        repeat, res = divmod(len_n, len_s)
        repeat += 1 if res else 0
        for idx in range(len_s * repeat):
            print("{}: {}".format(names[idx % len_n], songs[idx % len_s]))


if __name__ == '__main__':
    main()
