# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/5/594.pdf

Big-Little Endians conversion
"""

import struct
import sys


def main():
    records = sys.stdin.readlines()

    for rec in records:
        # 32-bit integer
        value = int(rec.strip())
        big_endian = (struct.unpack("<i", (struct.pack('>i', value))))[0]
        print("{} converts to {}".format(value, big_endian))


if __name__ == '__main__':
    main()
