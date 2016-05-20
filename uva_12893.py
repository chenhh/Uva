# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/128/12893.pdf
"""

def num(idx):
    if idx <= 1:
        return idx % 2
    else:
        return (num(idx//2)+(idx%2))
        
def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print (num(n))
        
if __name__ == '__main__':
    main()