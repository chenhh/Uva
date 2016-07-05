# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/3/389.pdf
"""

import sys


def int_to_str(n, base):
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = []
    while n > 0:
        output.append(symbols[n % base])
        n //= base
    return "".join(reversed(output))


def main():
    recs = iter(sys.stdin.readlines())
    while True:
        try:
            digits, src, tgt = next(recs).split()
            src_base = int(src)
            tgt_base = int(tgt)
            dec = int(digits, src_base)
            if dec == 0:
                print("{:>7}".format(0))
                continue

            res = int_to_str(dec, tgt_base)
            if len(res) > 7:
                print("{:>7}".format("ERROR"))
            else:
                print("{:>7}".format(res))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
