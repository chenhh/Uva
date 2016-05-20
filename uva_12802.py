# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/128/12802.pdf
"""

import array
BOUND = 10**6
def linear_sieve(N=BOUND):
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
    append = primes.append
    for idx in range(2, N+1):
        if sieves[idx]:
            append(idx)
        jdx = 0
        while (idx *primes[jdx] <= N):
            sieves[idx*primes[jdx]] = False
            if (idx % primes[jdx] == 0):
                break
            jdx += 1
            
    palindrome_primes = filter(palindrome, primes)
    return palindrome_primes

def palindrome(word):
    word = str(word)
    return all(word[idx] == word[len(word)-idx-1] for idx in range(len(word)//2))
 
def main():
    # add 1
    palindrome_primes = {
    1,2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 
    919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 
    13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181, 
    18481, 19391, 19891, 19991, 30103, 30203, 30403, 30703, 30803, 31013, 31513, 
    32323, 32423, 33533, 34543, 34843, 35053, 35153, 35353, 35753, 36263, 36563,
    37273, 37573, 38083, 38183, 38783, 39293, 70207, 70507, 70607, 71317, 71917, 72227, 
    72727, 73037, 73237, 73637, 74047, 74747, 75557, 76367, 76667, 77377, 77477,
    77977, 78487, 78787, 78887, 79397, 79697, 79997, 90709, 91019, 93139, 93239, 93739, 
    94049, 94349, 94649, 94849, 94949, 95959, 96269, 96469, 96769, 97379, 97579, 
    97879, 98389, 98689}
    
    while 1:
        n = int(input())
        print (n*2)
        if n in palindrome_primes:
            break

if __name__ == '__main__':
    #print (list(linear_sieve()))
    main()
