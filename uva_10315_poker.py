# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10315.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10315.htm
uva 451
"""

import sys

ranks = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


def hand_type(five_cards):
    global ranks
    # (rank, suit)
    sorted_cards = sorted(((ranks[v[0]], v[1]) for v in five_cards),
                          key=lambda x: (x[0], x[1]))
    values, suits = zip(*sorted_cards)

    is_flush = (suits[0] == suits[1] == suits[2] == suits[3] == suits[4])
    # (2,3, 4, 5, 6) ... (10,11,12,13,14)
    is_straight = all(values[idx] + 1 == values[idx + 1]
                      for idx in range(4))

    if is_straight and is_flush:
        # Straight flush:
        return (8, values)

    if ((values[0] == values[1] == values[2] == values[3]) or
            (values[1] == values[2] == values[3] == values[4])):
        # four of a kind
        return (7, values)

    if ((values[0] == values[1] == values[2] and values[3] == values[4]) or
            (values[0] == values[1] and values[2] == values[3] == values[4])):
        # Full House
        return (6, values)

    if is_flush:
        # flush
        return (5, values)

    if is_straight:
        # straight
        return (4, values)

    if ((values[0] == values[1] == values[2]) or
            (values[1] == values[2] == values[3]) or
            (values[2] == values[3] == values[4])):
        # three of a kind
        return (3, values)

    if (values[0] == values[1] and values[2] == values[3]):
        # two pairs
        return (2, (values[4], values[0], values[2]))

    if values[0] == values[1] and values[3] == values[4]:
        # two pairs
        return (2, (values[2], values[0], values[3]))

    if (values[1] == values[2] and values[3] == values[4]):
        # two pairs
        return (2, (values[0], values[1], values[3]))

    if values[0] == values[1]:
        # one pair
        return (1, (values[2], values[3], values[4], values[0]))

    if values[1] == values[2]:
        # one pair
        return (1, (values[0], values[3], values[4], values[1]))

    if values[2] == values[3]:
        # one pair
        return (1, (values[0], values[1], values[4], values[2]))

    if values[3] == values[4]:
        # one pair
        return (1, (values[0], values[1], values[2], values[3]))

    # nothing
    return (0, values)


def main():
    recs = sys.stdin.readlines()

    for rec in recs:
        cards = rec.split()
        b_type, b_values = hand_type(cards[:5])
        w_type, w_values = hand_type(cards[5:])
        if b_type > w_type:
            print("Black wins.")
        elif b_type < w_type:
            print("White wins.")
        else:
            if b_type in (8, 4):
                # Straight flush or straight
                b_val = max(b_values)
                w_val = max(w_values)
                if b_val > w_val:
                    print("Black wins.")
                elif b_val < w_val:
                    print("White wins.")
                else:
                    print("Tie.")

            elif b_type == 7:
                # four of a kind
                b_val = b_values[1]
                w_val = w_values[1]
                if b_val > w_val:
                    print("Black wins.")
                elif b_val < w_val:
                    print("White wins.")
                else:
                    print("Tie.")

            elif b_type in (3, 6):
                # Full House or three of a kind
                b_val = b_values[2]
                w_val = w_values[2]
                if b_val > w_val:
                    print("Black wins.")
                elif b_val < w_val:
                    print("White wins.")
                else:
                    print("Tie.")
            elif b_type in (0, 1, 2, 5):
                # flush, two_pairs, one_pair, nothing
                black_win = False
                white_win = False
                for idx in reversed(range(len(b_values))):
                    if b_values[idx] > w_values[idx]:
                        black_win = True
                        break
                    elif b_values[idx] < w_values[idx]:
                        white_win = True
                        break

                if black_win:
                    print("Black wins.")
                elif white_win:
                    print("White wins.")
                else:
                    print("Tie.")


if __name__ == '__main__':
    main()
