# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

10198 Counting

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/101/10198.pdf
f[n] = f[n-1] + f[n-2] + f[n-3] + f[n-1]

n=5
5 =  1 + 4 (1+ n-1)
  =  2 + 3 (2 + n-2)
  =  3 + 2 (3 + n-3)
  =  4 + 1 (4+n-1)

"""

import sys


def main():
    count = [0] * 1001
    count[0] = 1,
    count[1] = 2
    count[2] = 5
    count[3] = 13
    for idx in range(4, 1001):
        count[idx] = count[idx - 1] + count[idx - 2] + count[idx - 3] + count[
            idx - 1]

    recs = iter(sys.stdin.readlines())
    while True:
        try:
            val = int(next(recs))
            print(count[val])
        except (StopIteration):
            break


if __name__ == '__main__':
    main()
