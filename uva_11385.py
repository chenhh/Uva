# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/113/11385.pdf
"""


def main():
    fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
            1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,
            9227465, 14930352, 24157817, 39088169, 63245986, 102334155,
            165580141, 267914296, 433494437, 701408733, 1134903170,
            1836311903, 2971215073]
    fib_loc = {fib: idx for idx, fib in enumerate(fibs)}
    n_case = int(input())
    for _ in range(n_case):
        seqs_len = int(input())
        seqs = list(map(int, input().split()))
        code = input().strip()

        code_len = fib_loc[max(seqs)] + 1
        decode = [' '] * code_len
        # print(decode, len(decode))
        code_cdx = 0
        for c in code:
            if 'A' <= c <= 'Z':
                # print(seqs[code_cdx], fib_loc[seqs[code_cdx]], c)
                decode[fib_loc[seqs[code_cdx]]] = c
                code_cdx += 1
            if code_cdx == seqs_len:
                break

        print("".join(decode))


if __name__ == '__main__':
    main()
