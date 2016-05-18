# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/119/11934.pdf

f(n) = a*x^2 + b*x+ c
given a divisor d and a limit L
how many values f(0) to f(L) are divisible by d?

-1000 <= a, b, c <= 1000, 1 < d < < 1000000, 0 <= L < 1000
"""

def main():
    while 1:
       data = list(map(int, input().split()))
       if not any(data):
           break
       a, b, c, d, L = data
       # brute method
       print (sum(map(lambda x: 1 if not (a*x*x+b*x+c)%d else 0,
                      range(L+1))))

if __name__ == '__main__':
    main()




