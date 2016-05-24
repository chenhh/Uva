# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/120/12015.pdf
"""


def main():
    T = int(input())

    for tdx in range(T):
        urls = []
        max_score = 0
        for _ in range(10):
            url, score = input().split()
            score = int(score)
            if score > max_score:
                max_score = score
            urls.append((url, score))
        print("Case #{}:".format(tdx + 1))
        for url, score in urls:
            if score == max_score:
                print(url)


if __name__ == '__main__':
    main()
