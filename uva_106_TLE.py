# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/1/106.pdf
http://luckycat.kshs.kh.edu.tw/homework/q106.htm

https://zh.wikipedia.org/zh-tw/%E5%8B%BE%E8%82%A1%E5%AE%9A%E7%90%86

x^2 + y^2 = z^2
given (m,n) are positive integers.
x = m^2 - n^2
y= 2mn
z = m^2 + n^2

if (m, n) is relative prime, then (x, y, z) is also relative prime.
"""

import sys
from multiprocessing.pool import Pool

UPPER = 1000001


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y


def solve(val):
    n_rp_sol = 0
    not_used = [1] * val

    for m in range(1, 1000):
        for n in range(m + 1, UPPER, 2):
            if gcd(m, n) != 1:
                # not relative prime
                continue
            m2 = m * m
            n2 = n * n
            x = n2 - m2
            y = 2 * m * n
            z = m2 + n2

            if z > val:
                break

            n_rp_sol += 1

            # the mul of (kx, ky, kz) is still a solution
            # but the solutions are not relative prime.
            kx = x
            ky = y
            kz = z
            while kz <= val:
                not_used[kx - 1] = 0
                not_used[ky - 1] = 0
                not_used[kz - 1] = 0
                kx += x
                ky += y
                kz += z

    return (n_rp_sol, sum(not_used))


def sequential_main():
    recs = iter(sys.stdin.readlines())
    for rec in recs:
        val = int(rec)
        v1, v2 = solve(val)

        print("{} {}".format(v1, v2))


def parallel_main():
    recs = sys.stdin.readlines()
    vals = [int(rec) for rec in recs]
    p = Pool()
    results = p.map(solve, vals)
    for v1, v2 in results:
        print("{} {}".format(v1, v2))


if __name__ == '__main__':
    sequential_main()
    # parallel_main()
