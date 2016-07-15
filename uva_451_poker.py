# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

http://luckycat.kshs.kh.edu.tw/homework/q451.htm
https://uva.onlinejudge.org/external/4/451.pdf

uva 10315
"""

import sys

ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'X': 10, 'J': 11, 'Q': 12, 'K': 13}


def hand_type(five_cards):
    global ranks
    # (rank, suit)
    sorted_cards = sorted(((ranks[v[0]], v[1]) for v in five_cards),
                          key=lambda x: (x[0], x[1]))
    values, suits = zip(*sorted_cards)

    is_flush = (suits[0] == suits[1] == suits[2] == suits[3] == suits[4])
    # (1,2,3, 4, 5) or (1, 10, 11, 12, 13) or (1,2, 11, 12, 13) or
    # (1, 2, 3, 12, 13) or (1, 2, 3, 4, 13)
    is_straight = (all(values[idx] + 1 == values[idx + 1]
                       for idx in range(4)) or
                   (values[0] == 1 and values[1] == 10 and
                    values[2] == 11 and values[3] == 12 and
                    values[4] == 13) or
                   (values[0] == 1 and values[1] == 2 and
                    values[2] == 11 and values[3] == 12 and
                    values[4] == 13) or
                   (values[0] == 1 and values[1] == 2 and
                    values[2] == 3 and values[3] == 12 and
                    values[4] == 13) or
                   (values[0] == 1 and values[1] == 2 and
                    values[2] == 3 and values[3] == 4 and
                    values[4] == 13)
                   )

    if is_straight and is_flush:
        # Straight flush:
        return 8

    if ((values[0] == values[1] == values[2] == values[3]) or
            (values[1] == values[2] == values[3] == values[4])):
        # four of a kind
        return 7

    if ((values[0] == values[1] == values[2] and values[3] == values[4]) or
            (values[0] == values[1] and values[2] == values[3] == values[4])):
        # Full House
        return 6

    if is_flush:
        # flush
        return 5

    if is_straight:
        # straight
        return 4

    if ((values[0] == values[1] == values[2]) or
            (values[1] == values[2] == values[3]) or
            (values[2] == values[3] == values[4])):
        # three of a kind
        return 3

    if ((values[0] == values[1] and values[2] == values[3]) or
            (values[0] == values[1] and values[3] == values[4]) or
            (values[1] == values[2] and values[3] == values[4])):
        # two pairs, it can't be four and three of a kind
        return 2

    if ((values[0] == values[1]) or (values[1] == values[2]) or
            (values[2] == values[3]) or (values[3] == values[4])):
        # one pair
        return 1

    # nothing
    return 0


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        try:
            cards = []
            while True:
                data = next(recs).split()
                if data:
                    cards.append(data)
                else:
                    raise GeneratorExit

        except (GeneratorExit, StopIteration):
            stats = [0] * 9

            # print (cards)
            col_cards = [[0] * 5 for _ in range(5)]

            # by row
            for rdx, row in enumerate(cards):
                ht = hand_type(row)
                stats[ht] += 1
                for cdx in range(5):
                    col_cards[cdx][rdx] = row[cdx]

            # by col
            for col in col_cards:
                ht = hand_type(col)
                stats[ht] += 1

            if tdx:
                print()
            print(", ".join(map(str, stats)))


if __name__ == '__main__':
    main()
