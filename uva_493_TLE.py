# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1

https://uva.onlinejudge.org/external/4/493.pdf
http://luckycat.kshs.kh.edu.tw/homework/q493.htm

rational numbers are countable.
then b/a can be mapping to a unique positive integer.

N:1, E:1,
S:2, W:2,
N:3, E:3,
S:4, W:4,
N:5, E:5,
S:6, W:6,
...
"""

import sys
from array import array

ARR_SIZE = 500001


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while a % b:
        a, b = b, a % b
    return b


def is_valid_rational(a, b, rationals):
    """ b/a """
    if a == 0 or b == 0 or a == b:
        # zero and one has been visited
        return False

    com = gcd(a, b)
    if com != 1:
        # not relative prime
        a = a // com
        b = b // com

    if b < 0:
        a = -a
        b = -b

    value = '{}/{}'.format(a, b)
    if value in rationals:
        return False
    else:
        rationals.add(value)
        return True


def main():
    """ rational : y/x
    """

    x = array('l', [0] * ARR_SIZE)
    y = array('l', [0] * ARR_SIZE)
    x[0] = 1
    y[0] = 1
    x[1] = 1
    y[1] = 0

    rationals = set(("1/1", "0/1"))

    curr_x = 0
    curr_y = 0

    cnt = 0
    idx = 2
    while idx < ARR_SIZE:
        if cnt % 2:
            # North
            for jdx in range(1, cnt + 1):
                curr_y += 1
                if is_valid_rational(curr_x, curr_y, rationals):
                    # print (idx, "{}/{}".format(curr_y, curr_x))
                    x[idx] = curr_x
                    y[idx] = curr_y
                    idx += 1

                if idx >= ARR_SIZE:
                    break

            # East
            for jdx in range(1, cnt + 1):
                curr_x += 1
                if is_valid_rational(curr_x, curr_y, rationals):
                    # print(idx, "{}/{}".format(curr_y, curr_x))
                    x[idx] = curr_x
                    y[idx] = curr_y
                    idx += 1

                if idx >= ARR_SIZE:
                    break
        else:
            # South
            for jdx in range(1, cnt + 1):
                curr_y -= 1
                if is_valid_rational(curr_x, curr_y, rationals):
                    # print(idx, "{}/{}".format(curr_y, curr_x))
                    x[idx] = curr_x
                    y[idx] = curr_y
                    idx += 1

                if idx >= ARR_SIZE:
                    break

            # West
            for jdx in range(1, cnt + 1):
                curr_x -= 1
                if is_valid_rational(curr_x, curr_y, rationals):
                    # print(idx, "{}/{}".format(curr_y, curr_x))
                    x[idx] = curr_x
                    y[idx] = curr_y
                    idx += 1

                if idx >= ARR_SIZE:
                    break
        # update
        cnt += 1

    print(max(x), min(x))
    print(max(y), min(y))
    print("cache OK")

    recs = sys.stdin.readlines()
    for rec in recs:
        idx = int(rec)
        x_val = x[idx]
        y_val = y[idx]
        print(idx, x_val, y_val)
        if x_val < 0:
            print("{} / {}".format(-y_val / -x_val))
        else:
            print("{} / {}".format(y_val / x_val))


if __name__ == '__main__':
    main()
