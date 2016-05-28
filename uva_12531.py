# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12531.pdf

Note that when the minute hand moves, the hour hand may not move;
however, when the hour hand moves, the minute hand also moves

the hour and minute hands move discretely, the angle between the two hands
must be multiplier of 6.
"""


def main():
    while 1:
        try:
            angle = int(input())
            if angle % 6:
                print("N")
            else:
                print("Y")
        except (EOFError):
            break


if __name__ == '__main__':
    main()
