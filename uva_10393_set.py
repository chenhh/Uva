# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10393.pdf
"""

fingers = [
    'qaz', 'wsx', 'edc', 'rfvtgb', ' ', ' ', 'yhnujm', 'ik,', 'ol.', 'p;/',
]


def main():
    while 1:
        try:
            n_handicap, n_word = list(map(int, input().split()))
            # the unused fingers may not given in a line
            unused_fingers = []
            while len(unused_fingers) < n_handicap:
                unused_fingers.extend(list(map(int, input().split())))

            unused_char = frozenset("".join(fingers[v - 1]
                                            for v in unused_fingers))
            # print (unused_char)
            longest, candidate = 0, set()
            for _ in range(n_word):
                word = input().strip()
                is_ok = all(c not in unused_char for c in word)
                if is_ok:
                    if len(word) > longest:
                        longest = len(word)
                        candidate = {word, }
                    elif len(word) == longest:
                        candidate.add(word)
            print(len(candidate))
            for w in sorted(candidate):
                print(w)

        except (EOFError):
            break


if __name__ == '__main__':
    main()
