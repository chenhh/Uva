# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/162.pdf
"""

import sys
from collections import deque


def main():
    recs = iter(sys.stdin.readlines())
    cards = []
    cards_extend = cards.extend
    cards_clear = cards.clear
    tables = []
    tables_clear = tables.clear

    while True:
        data = next(recs).split()
        if data[0] == '#':
            break

        cards_extend(data)
        if len(cards) < 52:
            continue

        # processing
        # issue card to player first
        players = deque(card[1] for idx, card in enumerate(cards)
                        if idx % 2 == 0)
        dealers = deque(card[1] for idx, card in enumerate(cards)
                        if idx % 2)
        cards_clear()
        tables_clear()

        # 0: player, 1: dealer, player first
        turn = 0
        winner = -1

        while True:
            if not turn and not players:
                # players win
                winner = 0
                break

            if turn and not dealers:
                # dealers win
                winner = 1
                break

            # face up card and add it to the top of table
            curr_card = players.pop() if not turn else dealers.pop()
            tables.append(curr_card)

            # play switches
            turn = 1 - turn
            face_card_loop = False

            while curr_card in {'A', 'J', 'Q', 'K'}:
                face_card_loop = True
                cnt = 0
                if curr_card == 'A':
                    cnt = 4
                elif curr_card == 'J':
                    cnt = 1
                elif curr_card == 'Q':
                    cnt = 2
                elif curr_card == 'K':
                    cnt = 3

                for idx in range(cnt):
                    if not turn and not players:
                        # players win
                        winner = 0
                        break

                    if turn and not dealers:
                        # dealers win
                        winner = 1
                        break

                    # face up card and add it to the table
                    curr_card = players.pop() if not turn else dealers.pop()
                    tables.append(curr_card)

                    if curr_card in {'A', 'J', 'Q', 'K'}:
                        # play switch
                        break

                if winner >= 0:
                    # someone win the game
                    break
                # play switches
                turn = 1 - turn

            # end of face cards

            if winner >= 0:
                # someone win the game
                break

            if face_card_loop:
                # it has been into the face cards loop
                if not turn:
                    players.extend(tables[::-1])
                else:
                    dealers.extend(tables[::-1])
                tables.clear()

        print(winner, len(players), len(dealers))
        # winner, 0: player, 1: dealers
        print("{}{:3d}".format(
            2 - winner, len(players) if not winner else len(dealers)))


if __name__ == '__main__':
    main()
