# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/130/13012.pdf
""" 

def main():
    while 1:
        try:
            tea = int(input())
            ans = list(map(int, input().split()))
            correct = sum(tea == v for v in ans)
            print (correct)
        except:
            break

if __name__ == '__main__':
    main()