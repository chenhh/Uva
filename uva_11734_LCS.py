# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/117/11734.pdf
"""


def LCS(guess, answer):
    len_a, len_g = len(answer), len(guess)
    # shape:: len_a * len_g
    cost = [[0] * (len_g + 1) for _ in range(len_a + 1)]
    for adx in range(len_a):
        for gdx in range(len_g):
            if answer[adx] == guess[gdx]:
                cost[adx + 1][gdx + 1] = cost[adx][gdx] + 1
            else:
                cost[adx + 1][gdx + 1] = max(cost[adx + 1][gdx],
                                             cost[adx][gdx + 1])
    lcs = cost[len_a][len_g]

    if len_a == len_g == lcs:
        judge = "Yes"
    elif len_a != len_g and len_a == lcs:
        judge = "Output Format Error"
    else:
        judge = "Wrong Answer"
    return judge


def main():
    t = int(input())
    for tdx in range(t):
        guess = input()
        answer = input()
        judge = LCS(guess, answer)

        print("Case {}: {}".format(tdx + 1, judge))


if __name__ == '__main__':
    main()
