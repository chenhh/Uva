# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/127.pdf
http://luckycat.kshs.kh.edu.tw/homework/q127.htm

stack and double link list
it has about 25000 test cases.
read files requires about 0.72 secs.
"""

import sys
from multiprocessing.pool import Pool

def main():
    """
    correct, but TLE
    """
    recs = iter(sys.stdin.readlines())
    cards = []
    cards_clear = cards.clear
    cards_extend = cards.extend
    prev_pile_initialization = [idx - 1 for idx in range(52)]
    prev_pile_initialization[0] = None
    next_pile_initialization = [idx + 1 for idx in range(52)]
    next_pile_initialization[-1] = None

    while True:
        data = next(recs).split()
        if data[0] == '#':
            break

        cards_extend([[card, ] for card in data])

        if len(cards) < 52:
            continue

        # match: the same face value or the same suit
        n_pile = 52
        prev_pile = prev_pile_initialization[:]
        next_pile = next_pile_initialization[:]
        pos = 1
        while pos is not None:
            prev_pos = None
            prev3_pos = None
            if prev_pile[pos] is not None:
                prev_pos = prev_pile[pos]
                if (prev_pile[prev_pos] is not None and
                            prev_pile[prev_pile[prev_pos]] is not None):
                    prev3_pos = prev_pile[prev_pile[prev_pos]]

            curr_val, curr_suit = cards[pos][-1]
            if prev3_pos is not None:
                prev3_val, prev3_suit = cards[prev3_pos][-1]
                if curr_val == prev3_val or curr_suit == prev3_suit:
                    cards[prev3_pos].append(cards[pos].pop())

                    if not cards[pos]:
                        # delete the pos pile if the pile is empty
                        next_pile[prev_pos] = next_pile[pos]
                        if next_pile[pos] is not None:
                            prev_pile[next_pile[pos]] = prev_pos
                        n_pile -= 1
                    pos = prev3_pos
                    continue

            if prev_pos is not None:
                prev_val, prev_suit = cards[prev_pos][-1]
                if curr_val == prev_val or curr_suit == prev_suit:
                    cards[prev_pos].append(cards[pos].pop())

                    if not cards[pos]:
                        # delete the pos pile if the pile is empty
                        next_pile[prev_pos] = next_pile[pos]
                        if next_pile[pos] is not None:
                            prev_pile[next_pile[pos]] = prev_pos
                        n_pile -= 1
                    # if the immediate left is matched, the next round still
                    # match left 3 first (the pos must >= 1)
                    if prev3_pos is not None:
                        pos = prev3_pos
                    else:
                        pos = prev_pos
                    continue

            pos = next_pile[pos]

        # print (len(cards), cards)
        pile = n_pile
        print("{} {} remaining: {}".format(
            pile, "pile" if pile == 1 else "piles",
            " ".join(str(len(c)) for c in cards if c)))
        cards_clear()


def solve(piles):
    cards = [[card, ] for card in piles]

    # match: the same face value or the same suit
    n_pile = 52
    prev_pile = [idx - 1 for idx in range(52)]
    prev_pile[0] = None
    next_pile = [idx + 1 for idx in range(52)]
    next_pile[-1] = None
    pos = 1
    while pos is not None:
        prev_pos = None
        prev3_pos = None
        if prev_pile[pos] is not None:
            prev_pos = prev_pile[pos]
            if (prev_pile[prev_pos] is not None and
                        prev_pile[prev_pile[prev_pos]] is not None):
                prev3_pos = prev_pile[prev_pile[prev_pos]]

        curr_val, curr_suit = cards[pos][-1]
        if prev3_pos is not None:
            prev3_val, prev3_suit = cards[prev3_pos][-1]
            if curr_val == prev3_val or curr_suit == prev3_suit:
                cards[prev3_pos].append(cards[pos].pop())

                if not cards[pos]:
                    # delete the pos pile if the pile is empty
                    next_pile[prev_pos] = next_pile[pos]
                    if next_pile[pos] is not None:
                        prev_pile[next_pile[pos]] = prev_pos
                    n_pile -= 1
                pos = prev3_pos
                continue

        if prev_pos is not None:
            prev_val, prev_suit = cards[prev_pos][-1]
            if curr_val == prev_val or curr_suit == prev_suit:
                cards[prev_pos].append(cards[pos].pop())

                if not cards[pos]:
                    # delete the pos pile if the pile is empty
                    next_pile[prev_pos] = next_pile[pos]
                    if next_pile[pos] is not None:
                        prev_pile[next_pile[pos]] = prev_pos
                    n_pile -= 1
                # if the immediate left is matched, the next round still
                # match left 3 first (the pos must >= 1)
                if prev3_pos is not None:
                    pos = prev3_pos
                else:
                    pos = prev_pos
                continue

        pos = next_pile[pos]

    # print (len(cards), cards)
    pile = n_pile
    return ("{} {} remaining: {}".format(
        pile, "pile" if pile == 1 else "piles",
        " ".join(str(len(c)) for c in cards if c)))


def parallel_main():
    recs = iter(sys.stdin.readlines())
    pile_list = []
    while True:
        deck = next(recs).split()
        if deck[0] == '#':
            break
        deck += next(recs).split()
        pile_list.append((deck))
    # print (pile_list)

    p = Pool(6)
    results = p.map(solve, pile_list)
    for res in results:
        print(res)


if __name__ == '__main__':
    # main()
    parallel_main()
