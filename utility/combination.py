# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def permutation(N, M):
    """
    the answer is N!/M!
    N, M are both positive integer, and N>=M
    """
    #return reduce(lambda x,y: x*y, [v for v in range(N-M+1, M+1)])


def combination(N, M):
    """
    the answer is N!/M!/(N-M)!
    N, M are both positive integer
    """
    
def pascal_triangle(n_row):
    r1, r2 = [1], [1, 1]
    row = 1
    while row <= n_row:
        print(" ".join(map(str, r1)))
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
        row += 1


def gcd(x, y):
    while x % y:
        x, y = y, x % y
    return y
