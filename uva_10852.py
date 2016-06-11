# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/108/10852.pdf

given 100 <= n <= 10000, find the prime x <= n
such that n-p*x is maximum, where p*x <= n < (p+1)*x

n=4399, x=2203, p=1, n-p*x = 2196

the constraint 100 <= 100 is not correct!!
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
    sieves = array.array('B', [True] * (N + 1))
    sieves[0] = sieves[1] = False
    primes = array.array("L")

    for idx in range(2, N + 1):
        if sieves[idx]:
            primes.append(idx)
        jdx = 0
        while (idx * primes[jdx] <= N):
            sieves[idx * primes[jdx]] = False
            if (idx % primes[jdx] == 0):
                break
            jdx += 1
    return (sieves, primes)


def main():
    from time import time
    t = time()
    sieves, primes = linear_sieve(10000)

    answers = [0] * 100001
    for ndx in range(10001):
        max_res, x = 0, 0
        for prime in primes:
            if prime > ndx:
                break
            _, res = divmod(ndx, prime)
            if res >= max_res:
                max_res = res
                x = prime
        answers[ndx] = x

    n_case = int(input())
    for _ in range(n_case):
        n = int(input())
        print(answers[n])


if __name__ == '__main__':
    main()
