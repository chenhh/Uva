# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/748.pdf
"""

import sys


def main():
    records = sys.stdin.readlines()

    for rec in records:
        values = rec.strip().split()
        exp = int(values[1])
        # 95.123 => [95, 123]
        split_values = values[0].split('.')
        float_len = len(split_values[1]) * exp
        # 95.123 => 95123
        join_values = int("".join(split_values))

        product = str(join_values ** exp)

        if len(product) < float_len:
            # fill zero before the product
            product = "".join(['0' * (float_len - len(product)), product])

        # the dot_pos should not affect by the tail zeros
        dot_pos = len(product) - float_len

        # delete zeros in th tails
        tail_non_zero_pos = 0
        for idx, c in enumerate(reversed(product)):
            if c != '0':
                tail_non_zero_pos = idx
                break
        if tail_non_zero_pos != 0:
            product = product[:len(product) - tail_non_zero_pos]
        print("{}.{}".format(product[:dot_pos], product[dot_pos:]))


if __name__ == '__main__':
    main()
