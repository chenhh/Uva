# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/402.pdf
http://luckycat.kshs.kh.edu.tw/homework/q402.htm

10 2 3 5 4 3 2 9 6 10 10 6 2 6 7 3 4 7 4 5 3 2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
3 delete 3, 6, 9, remaining [1, 2, 4, 5, 7, 8, 10]
5 delete 7, remaining [1, 2, 4, 5, 8, 10]
4 delete 5, remaining [1, 2, 4, 8, 10]
3 delete 4, remaining [1, 2, 8 ,10]
2 delete 2 10, remaining [ 1, 8] #
"""


def survival_location(n_people, n_winner, pokes):
    """
    n_people: positive integer
    n_winner: positive integer
    pokes: list of integer
    """
    survival = [1] * n_people
    n_survival = n_people
    finished = False

    # there are at most 20 cards
    for cdx, card in enumerate(pokes):
        cnt = 0
        if finished:
            break
        for idx, val in enumerate(survival):
            if n_survival <= n_winner:
                finished = True
                break

            if val == 1:
                cnt += 1
                if cnt % card == 0:
                    survival[idx] = 0
                    n_survival -= 1
                    # print (card, n_survival)
                    # print ([idx+1 for idx, val in enumerate(survival) if val == 1])

    return [str(idx + 1) for idx, val in enumerate(survival) if val == 1]


def main():
    case = 0
    while 1:

        try:
            values = list(map(int, input().split()))
            # 1<=50<=N, 1<=X<=N, 1<=value<=11 in pokes
            n_people, n_winner, pokes = values[0], values[1], values[2:]

            ans = survival_location(n_people, n_winner, pokes)
            case += 1
            print("Selection #{}".format(case))
            print(" ".join(ans))
            # empty line between two consecutive cases
            print("")
        except (EOFError):
            break


if __name__ == '__main__':
    main()
