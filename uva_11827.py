# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/118/11827.pdf
"""

def gcd(a, b):
    if b == 0:
       return a
    else:
       return gcd(b, a % b)

def main():
    N = int(input())
    for _ in range(N):
        data = list(map(int, input().split()))
        data_len = len(data)
        max_gcd = 0
        for idx in range(data_len):
            for jdx in range(idx+1, data_len):
                val = gcd(data[idx], data[jdx])
                if val > max_gcd:
                    max_gcd = val
        print (max_gcd)

if __name__ == '__main__':
    main()