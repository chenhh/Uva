# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11917.pdf
"""

def main():
    # number of test cases
    T = int(input())
    for tdx in range(T):
        # number of subjects
        N = int(input())
        subjects = {}
        for ndx in range(N):
            name, day = input().split()
            subjects[name] = int(day)
        D = int(input())
        homework = input().strip()

        if homework in subjects.keys():
            required = subjects[homework]
            if required <= D:
                ans = "Yesss"
            elif D < required <= D+5:
                ans = "Late"
            else:
                ans = "Do your own homework!"
        else:
            ans = "Do your own homework!"
        print ("Case {}: {}".format(tdx+1, ans))

if __name__ == '__main__':
    main()