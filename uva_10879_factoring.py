# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/108/10879.pdf
"""

import array
import sys

UPPER = 10000000
SQRT_UPPER = 3163


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
    sieves = array.array('B', [True] * (N + 1))
    sieves[0] = sieves[1] = False
    primes = array.array("L")

    for idx in range(2, N + 1):
        if sieves[idx]:
            primes.append(idx)
        jdx = 0
        while (idx * primes[jdx] <= N):
            sieves[idx * primes[jdx]] = False
            if not idx % primes[jdx]:
                break
            jdx += 1
    return (sieves, primes)


def main():
    sieves, primes = linear_sieve(SQRT_UPPER)

    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        value = int(next(recs))
        K = value
        factors = []
        for p in primes:
            while not K % p:
                factors.append(p)
                K //= p
            if K == 1:
                break

        ans = []
        K2 = value
        m1 = 1
        for f in factors:
            m1 *= f
            m2 = K2 // m1
            if m1 not in ans and m2 not in ans:
                ans.append(m1)
                ans.append(m2)

            if len(ans) >= 4:
                break

        print("Case #{}: {} = {} * {} = {} * {}".format(
            tdx + 1, value, ans[0], ans[1], ans[2], ans[3]
        ))


if __name__ == '__main__':
    main()
