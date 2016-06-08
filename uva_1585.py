# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/15/1585.pdf
"""


def main():
    scores = []
    scores_append = scores.append

    n_case = int(input())
    for _ in range(n_case):
        data = input().strip()
        scores.clear()
        scores_append(0 if data[0] == 'X' else 1)
        for ans in data[1:]:
            if ans == 'O':
                scores_append(1 + scores[-1])
            else:
                scores_append(0)

        # print (scores)
        print(sum(scores))


if __name__ == '__main__':
    main()
