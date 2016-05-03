# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/5/583.pdf
there are 6542 primes between 0~65536
"""

import array

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

def factor_tables():
    factors = {
        4:{2: 2}, 6:{2:1, 3:1}}

def main():
    # 65536 = 2**16
    BOUND = 65536
    sieves, primes = linear_sieve(BOUND)

    while True:
        value = int(input())
        if value == 0:
            break

        factors = []
        if value < 0:
            factors.append(-1)
        tmp = abs(value)

        if tmp <= BOUND and sieves[tmp]:
            # prime
            factors.append(tmp)
        else:
            # tmp > BOUND or tmp is composite
            idx = 0
            while tmp >= 1 :
                while tmp % primes[idx] == 0:
                    tmp //= primes[idx]
                    factors.append(primes[idx])
                idx += 1

        print ("{} = {}".format(value, " x ".join(str(v)for v in factors)))

if __name__ == '__main__':
    main()