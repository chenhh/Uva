# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/288.pdf
"""

import sys


def main():
    recs = sys.stdin.readlines()
    for rec in recs:
        print (eval(rec.strip()))

if __name__ == '__main__':
    main()