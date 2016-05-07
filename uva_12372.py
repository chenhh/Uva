# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/123/12372.pdf
"""

def main():
    T = int(input())
    for tdx in range(T):
        sizes = list(map(int, input().split()))
        print ("Case {}: {}".format(
            tdx+1, "good" if max(sizes) <= 20 else "bad"))

if __name__ == '__main__':
    main()