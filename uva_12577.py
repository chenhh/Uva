# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12577.pdf
"""

import sys


def main():
    records = sys.stdin.readlines()

    for idx, line in enumerate(records):
        word = line.strip()
        if word == '*':
            break
        print ("Case {}: {}".format(idx+1,
            "Hajj-e-Akbar" if word == "Hajj" else "Hajj-e-Asghar"))


if __name__ == '__main__':
    main()