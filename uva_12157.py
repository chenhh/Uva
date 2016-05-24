# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/121/12157.pdf

Mile charges every 30 seconds at a rate of 10 cents.
Juice charges every 60 seconds at a rate of 15 cents.
"""


def main():
    T = int(input())
    for tdx in range(T):
        n = int(input())
        secs = list(map(int, input().split()))
        Mile = Juice = 0
        for sec in secs:
            Mile += (sec//30 + 1) * 10
            Juice += (sec//60 + 1) * 15
        print ("Case {}: ".format(tdx+1), end="")
        if Mile == Juice:
            print ("Mile Juice {}".format(Mile))
        elif Mile < Juice:
            print ("Mile {}".format(Mile))
        else:
            print ("Juice {}".format(Juice))

if __name__ == '__main__':
    main()