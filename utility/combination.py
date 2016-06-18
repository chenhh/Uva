# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def permutation(nodes):
    """
    http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

    Parameters:
    ----------------------------------
    nodes: list or string

    Return:
    ----------------------------------
    list of all permutations
    """
    n_node = len(nodes)
    stack = [(nodes, 0), ]
    ans = []
    while stack:
        # print ("stack:", stack)
        curr, loc = stack.pop()
        # print (loc, curr)
        if loc == n_node - 1:
            ans.append(curr)
            continue
        for jdx in range(loc, n_node):
            curr[jdx], curr[loc] = curr[loc], curr[jdx]
            # copy on value, not copy on reference
            stack.append([curr[:], loc + 1])
            curr[jdx], curr[loc] = curr[loc], curr[jdx]
    return (ans[::-1])

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
