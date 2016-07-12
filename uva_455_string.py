# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/455.pdf
http://luckycat.kshs.kh.edu.tw/homework/q455.htm
"""

import sys

sieves = (0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
          1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0,
          0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
          0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
          0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
          0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
          0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
          0, 0, 1, 0, 0)
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
          61, 67, 71, 73, 79)


def prime_main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        while True:
            data = next(recs).strip('\n')
            if data:
                break

        if tdx:
            print()

        len_data = len(data)
        if sieves[len_data]:
            # the length is a prime number
            print(len_data)
            continue

        # # check the factors
        if data == data[0] * len_data:
            print(1)
            continue

        tmp = len_data
        len_sub = 1
        min_len_sub = 1
        ans = False

        factors = set()
        for prime in primes:
            if ans:
                break
            while not tmp % prime:
                len_sub *= prime
                repeat = len_data // len_sub
                factors.add(len_sub)
                factors.add(repeat)
                tmp //= prime
            if tmp == 1:
                break

        factors = sorted(list(factors))
        for len_sub in factors:
            repeat = len_data // len_sub
            if data[:len_sub] * repeat == data:
                min_len_sub = len_sub
                break

        print(min_len_sub)

def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for tdx in range(n_case):
        while True:
            data = next(recs).strip('\n')
            if data:
                break

        if tdx:
            print()

        len_data = len(data)
        for idx in range(1, len_data + 1):
            if not (len_data % idx):
                repeat = len_data // idx
                if data == data[:idx] * repeat:
                    print(idx)
                    break

if __name__ == '__main__':
    main()