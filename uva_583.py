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
    from time import time
    t = time()
    BOUND = 65536
    import os

    sieves, primes = linear_sieve(BOUND)
    factors = {}
    for value in range(2, BOUND+1):
        if sieves[value]:
            factors[value] = [value,]
        else:
            # composite
            tmp = value
            idx = 0
            factors[value] = []
            while primes[idx] * primes[idx] <= value:
                while (tmp >= 1 and tmp % primes[idx] == 0):
                    tmp = tmp // primes[idx]
                    factors[value].append(primes[idx])
                idx += 1
            if tmp != 1:
                factors[value].append(tmp)
        print ("{}: {}, ".format(value, factors[value]))
    print (time()-t)


    # while True:
    #     value = int(input())
    #     if value == 0:
    #         break
    #
    #     outputs = []
    #     if value < 0:
    #         outputs.append(-1)
    #     tmp = abs(value)
    #
    #     if tmp <= BOUND:
    #         outputs.extend(factors[tmp])
    #     else:
    #         # tmp > BOUND
    #         while primes[idx] * primes[idx] <= abs(value):
    #             while (tmp >= 1 and tmp % primes[idx] == 0):
    #                 tmp //= primes[idx]
    #             idx += 1
    #
    #         # tmp is prime and > BOUND
    #         if tmp > BOUND:
    #             factors.append(str(tmp))
    #
    #     factor_str = " x ".join(factors)
    #     print ("{} = {}".format(value, factor_str))

if __name__ == '__main__':
    main()