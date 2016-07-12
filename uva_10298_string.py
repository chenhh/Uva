# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/102/10298.pdf
the same problem as uva 455
"""

import sys


def main():
    recs = sys.stdin.readlines()

    for rec in recs:
        data = rec.strip('\n')
        if data == '.':
            break

        len_data = len(data)
        for idx in range(1, len_data + 1):
            if not (len_data % idx):
                repeat = len_data // idx
                if data == data[:idx] * repeat:
                    print(repeat)
                    break


if __name__ == '__main__':
    main()
