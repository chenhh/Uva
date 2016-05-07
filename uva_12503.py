# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/125/12503.pdf
"""


def main():
    T = int(input())

    for _ in range(T):
        p = int(input())

        loc = 0
        actions = []
        for _ in range(p):
            cmd = input().strip()
            mov = cmd.split()
            if len(mov) == 1:
                act = mov[0]
            else:
                act = actions[int(mov[2]) - 1]
            actions.append(act)

            if act == 'LEFT':
                loc -= 1
            elif act == 'RIGHT':
                loc += 1

        print(loc)


if __name__ == '__main__':
    main()
