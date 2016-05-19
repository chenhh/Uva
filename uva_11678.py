# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/116/11678.pdf

They obviously don’t care about identical cards they both have, and
they don’t want to receive repeated cards in the trade.

The cards are traded in a single operation: Alice gives Betty N distinct
cards and receives back other N distinct cards.

Alice: {1, 1, 2, 3, 5, 7, 8, 8, 9, 15}
Betty: {2, 2, 2, 3, 4, 6, 10, 11, 11}
answer: 4
    A->B: {1, 5,6, 8, 9, 15}
    B->A: {4, 6, 10, 11}
"""

def main():
    while 1:
        n_A, n_B = list(map(int, input().split()))
        if n_A == 0 and n_B == 0:
            break

        # non-descending order
        A_cards = set(map(int, input().split()))
        B_cards = set(map(int, input().split()))
        ans = min(len(A_cards - B_cards), len(B_cards - A_cards))
        print (ans)

if __name__ == '__main__':
    main()