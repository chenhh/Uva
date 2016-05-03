# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/5/583.pdf
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
    return (sieves, frozenset(primes))


def main():
    # 65536 = 2**16
    sieves, primes = linear_sieve(65536)

    prime_set = frozenset(primes)
    n_primes = len(primes)

    while True:
        value = int(input())
        if value == 0:
            break

        tmp = abs(value)
        if tmp in prime_set:
            if value > 0:
                print ("{} = {}".format(value, value))
            else:
                print("{} = -1 x {}".format(value, tmp))
        else:
            prime_dict={}
            for idx, prime in enumerate(primes):
                while (tmp >= 1 and tmp % prime == 0):
                    tmp //=prime
                    if prime in prime_dict.keys():
                        prime_dict[prime] += 1
                    else:
                        prime_dict[prime] = 1



if __name__ == '__main__':
    main()