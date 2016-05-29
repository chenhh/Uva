# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1

https://uva.onlinejudge.org/external/4/402.pdf
http://luckycat.kshs.kh.edu.tw/homework/q402.htm
"""

import sys


def survival_location(n_people, n_winner, pokes):
    # people list store the location of next person
    people = list(range(1, n_people + 1))
    head, prev, tail = 0, n_people - 1, 0
    people[-1] = 0
    n_loser = n_people

    for card in pokes:
        for idx in range(n_people):
            for jdx in range(card - 1):
                prev = head
                head = people[head]
            tail = head
            # update link list, skip the tail element
            people[prev] = people[head]
            head = people[head]

            # delete tail element
            people[head] = -1


def main():
    records = sys.stdin.readlines()

    for idx, rec in enumerate(records):
        values = list(map(int, rec.strip().split()))
        # 1<=50<=N, 1<=X<=N, 1<=value<=11 in pokes
        n_people, n_winner, pokes = values[0], values[1], values[2:]

        if idx:
            # empty line between two consecutive cases
            print("")

        ans = survival_location(n_people, n_winner, pokes)
        print("Selection #{}".format(idx + 1))
        print("".join(ans))


if __name__ == '__main__':
    main()
