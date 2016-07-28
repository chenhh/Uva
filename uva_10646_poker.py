# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

10646 What is the Card?

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/106/10646.pdf
"""

import sys


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    piles = []
    piles_extend = piles.extend
    piles_clear = piles.clear

    for tdx in range(n_case):
        try:
            piles_clear()

            while True:
                piles_extend(next(recs).split())
                if len(piles) >= 52:
                    break
            hands = piles[27:]
            cards = piles[:27]

            Y = 0
            for _ in range(3):
                card = cards.pop()
                X = int(card[0]) if '1' <= card[0] <= '9' else 10
                Y += X
                for _ in range(10 - X):
                    cards.pop()

            cards.extend(hands)
            # print ("Y=", Y)
            print("Case {}: {}".format(tdx + 1, cards[Y - 1]))

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
