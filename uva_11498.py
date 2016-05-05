# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/114/11498.pdf
"""

def main():

    while True:
        K = int(input())
        if K == 0:
            break

        origins = list(map(int, input().split()))
        for _ in range(K):
            points = list(map(int, input().split()))

            if points[0] == origins[0] or points[1] == origins[1]:
                # boundary
                print ("divisa")
            elif points[0] < origins[0] and points[1] > origins[1]:
                # north west
                print ("NO")
            elif points[0] > origins[0] and points[1] > origins[1]:
                # north east
                print ("NE")
            elif points[0] > origins[0] and points[1] < origins[1]:
                # south east
                print ("SE")
            elif points[0] < origins[0] and points[1] < origins[1]:
                # south west
                print ("SO")

if __name__ == '__main__':
    main()