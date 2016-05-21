# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/126/12694.pdf
http://luckycat.kshs.kh.edu.tw/homework/q12694.htm

greedy, shortest conference first then collision detection
"""
import operator

def main():
    T = int(input())
    meetings = []
    for _ in range(T):
        meetings.clear()
        while 1:
            pairs = list(map(int, input().split()))
            if any(pairs):
                meetings.append([pairs[0], pairs[1], pairs[1]- pairs[0]])
            else:
                # all zeros
                break
        # shortest conference check first
        meetings.sort(key=operator.itemgetter(2))
        # print (meetings)

        # collision detection
        count = 0
        hours = [True for _ in range(10)]
        for start, final, period in meetings:
            if all(hours[start:final]):
                for jdx in range(start, final):
                    hours[jdx] = False
                count += 1
        print (count)

if __name__ == '__main__':
    main()