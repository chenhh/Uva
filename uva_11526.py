# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11526.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11526.htm
"""
import math

def orig_H(n):
    """
    if n is a very large number, it will TLE
    e.g. n= 2**31-1, complexity: O(n)
    """
    return sum(n//idx for idx in range(1, n+1))

def H(n):
    """ complexity : O(lg n) """
    if n <=0:
        return 0
    root = int(math.sqrt(n)) + 1
    res = sum(n//idx for idx in range(1, root))
    root -= 1
    res = res*2 - root*root
    return res


def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(H(n))


if __name__ == '__main__':
    main()