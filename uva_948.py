# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/9/948.pdf
"""

import bisect


def fibbonacci(UPPER=100000000):
    """
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
    2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
    317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
    14930352, 24157817, 39088169, 63245986, 102334155]
    """
    seqs = [1, 1]
    # value = 1
    while seqs[-1] <= UPPER:
        seqs.append(seqs[-1] + seqs[-2])
    return (seqs)


def main():
    fibs = fibbonacci()

    n_case = int(input())
    for _ in range(n_case):
        value = int(input())
        tmp = value
        positions = []
        while tmp > 0:
            fib_idx = bisect.bisect_right(fibs, tmp) - 1
            tmp -= fibs[fib_idx]
            positions.append(fib_idx)

        # print (value, positions)
        code = ['0'] * positions[0]
        for pos in positions:
            code[pos - 1] = '1'
        print("{} = {} (fib)".format(value, ''.join(reversed(code))))


if __name__ == '__main__':
    main()
