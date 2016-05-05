# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
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


def is_prime(N):
    """
    Parameter:
    -----------
    N: positive integer

    Return:
    -----------
    True is N is a prime, else False
    """
    if N <= 1:
        return False
    elif N ==2 or N == 3:
        return True
    elif not (N % 2):
        return False
    else:
        idx = 3
        prime = True
        while (idx*idx <= N):
            if not(N % idx):
                prime = False
                break
            idx += 1
        return prime

def test_prime(N):

    sieves, primes = linear_sieve(N)
    print (sieves)
    print (primes)
    correct = True
    for idx in range(N+1):
        if sieves[idx] != is_prime(idx):
            print ("{} errors.".format(idx))
            correct = False
    if correct:
        print ("all results from 0 to {} are correct.".format(N))

def square_root(Y):
    """
    for big number
    """
    EPS = 1e-3
    a, b = 1, Y
    while (abs(a-b)>EPS):
        a = (a+b)//2
        b = Y//a
    return a


if __name__ == '__main__':
    test_prime(65536)