# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11530.pdf
"""

keymap = {
    'a': 1, 'b': 2, 'c': 3,
    'd': 1, 'e': 2, 'f': 3,
    'g': 1, 'h': 2, 'i': 3,
    'j': 1, 'k': 2, 'l': 3,
    'm': 1, 'n': 2, 'o': 3,
    'p': 1, 'q': 2, 'r': 3, 's': 4,
    't': 1, 'u': 2, 'v': 3,
    'w': 1, 'x': 2, 'y': 3, 'z': 4,
    ' ': 1
}


def main():
    n_case = int(input())
    for tdx in range(1, n_case + 1):
        data = input()
        print("Case #{}: {}".format(tdx, sum(keymap[c] for c in data)))


if __name__ == '__main__':
    main()
