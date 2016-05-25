# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/119.pdf
"""


def main():
    case = 0
    while 1:
        try:
            n_people = int(input())
            names = input().split()
            amount = {}
            get = amount.get
            for _ in range(len(names)):
                act = input().split()
                giver, total, n_receiver = act[0], int(act[1]), int(act[2])
                if n_receiver:
                    value = total // n_receiver
                    amount[giver] = get(giver, 0) + -value * n_receiver
                    for receiver in act[3:]:
                        amount[receiver] = get(receiver, 0) + value
            if case:
                print("")

            case += 1
            for name in names:
                print("{} {}".format(name, amount.get(name, 0)))

        except (EOFError):
            break


if __name__ == '__main__':
    main()
