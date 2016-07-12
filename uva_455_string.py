# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/455.pdf
http://luckycat.kshs.kh.edu.tw/homework/q455.htm
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        while True:
            data = next(recs).strip('\n')
            if data:
                break

        if tdx:
            print()

        len_data = len(data)
        for idx in range(1, len_data + 1):
            if not (len_data % idx):
                repeat = len_data // idx
                if data == data[:idx] * repeat:
                    print(idx)
                    break


if __name__ == '__main__':
    main()
