# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/105/10551.pdf
"""

import sys


def int_to_str(n, base):
    """ uva 389 """
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = []
    while n > 0:
        output.append(symbols[n % base])
        n //= base
    if not output:
        return "0"
    return "".join(reversed(output))


def main():
    recs = iter(sys.stdin.readlines())
    for rec in recs:
        values = rec.split()
        if values[0] == '0':
            break
        base = int(values[0])

        dec1 = int(values[1], base)
        dec2 = int(values[2], base)
        mod = int_to_str(dec1 % dec2, base)
        print(mod)


if __name__ == '__main__':
    main()
