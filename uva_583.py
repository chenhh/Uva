# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2

https://uva.onlinejudge.org/external/5/583.pdf
there are 6542 primes between 0~65536
The python version must be TLE

"""

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
    sieves = [True]*(N+1)
    sieves[0] = sieves[1] = False
    primes = []

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
    from time import time
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

        if tmp == 1:
            factors.append(1)
        elif tmp <= BOUND and sieves[tmp]:
            factors.append(tmp)
        else:
            idx = 0
            abs_value = abs(value)
            while tmp > 1 and primes[idx] * primes[idx] <= abs_value:
                while tmp % primes[idx] == 0:
                    tmp //= primes[idx]
                    factors.append(primes[idx])

                if tmp <= BOUND and sieves[tmp]:
                    factors.append(tmp)
                    break
                idx += 1
            # tmp is a prime
            if tmp > BOUND:
                factors.append(tmp)

        print("{} = {}".format(value,
                    " x ".join(str(v) for v in factors)))

if __name__ == '__main__':
    main()
