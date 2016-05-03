# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/1/160.pdf
prime and factor decomposition
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

def main():
    sieves, primes = linear_sieve(100)

    while True:
        N = int(input())
        if N == 0:
            break
        prime_cnt = [0] * (N+1)

        for fact in range(2, N+1):
            if sieves[fact]:
                # prime
                prime_cnt[fact] += 1
            else:
                # not a prime, do factor decomposition
                tmp = fact
                for prime in primes:
                    while tmp >=2 and tmp % prime == 0:
                        prime_cnt[prime] += 1
                        tmp //= prime
        print ("{:>3d}! =".format(N), end="")
        elements = [cnt for cnt in prime_cnt if cnt != 0]
        n_element = len(elements)
        if n_element <= 15:
            print ("".join("{:>3d}".format(v) for v in elements))
        else:
            rows = n_element // 15
            rows += 0 if n_element % 15 == 0 else 1
            for rdx in range(rows):
                if rdx == 0:
                    print("".join("{:>3d}".format(v) for v in elements[:15]))
                else:
                    print("      {}".format(
                        "".join("{:>3d}".format(v)
                                for v in elements[rdx*15:(rdx+1)*15])))

if __name__ == '__main__':
    main()