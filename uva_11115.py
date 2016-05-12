# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/111/11115.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11115.htm
D different balls put to N different boxes

https://en.wikipedia.org/wiki/Stirling_number
D different balls put to N the same boxes, and there are some boxes empty.
S(D,1)+ ... + S(D, N)

"""

def main():
    while 1:
        N, D = list(map(int, input().split()))
        if N== 0 and D == 0:
            break