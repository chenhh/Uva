# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/121/12136.pdf
"""

from datetime import datetime

def main():
    N = int(input())

    for ndx in range(N):
        t1s = input().split()
        t2s = input().split()

        wifes = []
        for t in t1s:
            h, m =list(map(int, t.split(":")))
            wifes.append(datetime(2016,5,8,h,m))

        meetings = []
        for t in t2s:
            h, m = list(map(int, t.split(":")))
            meetings.append(datetime(2016,5,8, h, m))

        hits = True
        if (wifes[0] <= meetings[0] <= wifes[1] or
            wifes[0] <= meetings[1] <= wifes[1]):
            # intersection
            hits = False
        elif (wifes[0] >= meetings[0] and wifes[1] <= meetings[1]):
            # containing
            hits = False

        print ("Case {}: {} Meeting".format(ndx+1, "Hits" if hits else "Mrs"))

if __name__ == '__main__':
    main()