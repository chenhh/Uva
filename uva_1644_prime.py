# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/16/1644.pdf
"""

import array
import bisect

def linear_sieve(N):
    """
    Parameter:
    ---------------------
    N, positive integer, build the prime table from 0 to N.

    Returns:
    ---------------------
    sieves, array: if jdx is a prime, then sieves[jdx] is True
    primes, array: all primes less than N
    """
    sieves = array.array('B', [True]*(N+1))
    sieves[0] = sieves[1] = False
    primes = array.array("L")

    for idx in range(2, N+1):
        if sieves[idx]:
            primes.append(idx)
        jdx = 0
        while (idx *primes[jdx] <= N):
            sieves[idx*primes[jdx]] = False
            if (idx % primes[jdx] == 0):
                break
            jdx += 1
    return (sieves, primes)


def main():
    BOUND = 1299709
    sieves, primes = linear_sieve(BOUND)

    while 1:
        val = int(input())
        if not val:
            break
        if sieves[val] or val == 1:
            print (0)
        else:
            sdx = bisect.bisect_left(primes, val)
            print (primes[sdx] - primes[sdx-1])


if __name__ == '__main__':
    main()