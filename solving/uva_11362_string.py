# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/113/11362.pdf

only a short value can be prefix of a long value
"""
from operator import itemgetter


def TLE_main():
    n_case = int(input())
    for _ in range(n_case):
        n_num = int(input())
        nums = [input().strip() for _ in range(n_num)]
        # sort by len then by alphabet
        num_lens = sorted([(v, len(v)) for v in nums], key=itemgetter(1))
        # print (num_lens)
        min_len, max_len = num_lens[0][1], num_lens[-1][1]

        consistent = True
        for idx in range(n_num):
            if num_lens[idx][1] == max_len or not consistent:
                # the longest number can't be prefix of any others
                break
            for jdx in range(idx + 1, n_num):
                if num_lens[idx][1] == num_lens[jdx][1]:
                    # two numbers with the same length can't be prefix
                    continue
                # the idx length must less than jdx length
                prefix_len = num_lens[idx][1]
                if num_lens[idx][0] == num_lens[jdx][0][:prefix_len]:
                    consistent = False
                    break
        print("YES" if consistent else "NO")


def main():
    n_case = int(input())
    for _ in range(n_case):
        n_num = int(input())
        nums = sorted(input().strip() for _ in range(n_num))
        num_lens = sorted([(v, len(v)) for v in nums], key=itemgetter(1))
        print(num_lens)


if __name__ == '__main__':
    main()
