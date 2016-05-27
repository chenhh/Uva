# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1

https://uva.onlinejudge.org/external/1/170.pdf
http://luckycat.kshs.kh.edu.tw/homework/q170.htm

the input of cards are from pile K, Q, J, T, ... to 1, and from top to bottom.
there are at least 4 cards will be used. (KS, KH, KC and KD in pile K)
"""

from collections import deque


def main():
    n_card = 0
    piles = [deque() for _ in range(13)]
    num_map = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    while 1:
        cards = input().split()
        if cards[0] == '#':
            break
        # input
        for idx, card in enumerate(cards):
            # True: head, False: tail
            piles[12 - idx].append([card, False])
            n_card += 1

        if n_card == 52:
            # takes a card from top of pile K
            curr = piles[-1].popleft()

            for cnt in range(1, 53):
                # set the card is used
                curr[1] = True
                # parse card number
                card_num = num_map[curr[0][0]]
                piles[card_num - 1].append(curr)
                if piles[card_num - 1][0][1]:
                    # all the cards in the pile are visited
                    break
                # take card from top of the pile
                curr = piles[card_num - 1].popleft()
            print("{:02d},{}".format(cnt, curr[0]))

            # clear
            piles = [deque() for _ in range(13)]
            n_card = 0


if __name__ == '__main__':
    main()
