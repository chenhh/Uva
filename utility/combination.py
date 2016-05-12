# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""
from functools import reduce

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