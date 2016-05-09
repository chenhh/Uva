# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/117/11777.pdf
"""

def main():
    T = int(input())

    for tdx in range(T):
        scores = list(map(int, input().split()))
        class_score = sum(v for idx, v in enumerate(sorted(scores[4:]))
                         if idx >=1)/2
        total = sum(scores[:4]) + class_score
        if total >= 90:
            grade ='A'
        elif 80 <= total < 90:
            grade = 'B'
        elif 70 <= total < 80:
            grade = 'C'
        elif 60 <= total <70:
            grade = 'D'
        else:
            grade = 'F'
        print ("Case {}: {}".format(tdx+1, grade))

if __name__ == '__main__':
    main()