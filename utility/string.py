# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def LIS(seqs):
    """
    Robinson-Schensted-Knuth Algorithm
    to find the last occurrence of the LIS
    """
    import bisect
    n_data = len(seqs)
    tmp_lis = [seqs[0], ]
    pos = [1] * n_data
    for idx in range(1, n_data):
        if seqs[idx] > tmp_lis[-1]:
            tmp_lis.append(seqs[idx])
            pos[idx] = len(tmp_lis)
        else:
            # strictly increasing,
            loc = bisect.bisect_left(tmp_lis, seqs[idx])
            tmp_lis[loc] = seqs[idx]
            pos[idx] = loc + 1

    # traceback
    lis_len = len(tmp_lis)
    lis = [0] * lis_len
    kdx = lis_len
    for jdx in reversed(range(n_data)):
        if pos[jdx] == kdx:
            lis[kdx - 1] = seqs[jdx]
            kdx -= 1

    return lis


def lcs(line1, line2):
    """
    line1: list of words, the first word is empty.
    line2: list of words, the first word is empty.
    """
    len1 = len(line1)
    len2 = len(line2)
    # n_row: len2, n_col: len1
    length = [[0] * len2 for _ in range(len1)]
    for idx in range(1, len1):
        for jdx in range(1, len2):
            if line1[idx] == line2[jdx]:
                length[idx][jdx] = length[idx - 1][jdx - 1] + 1
            else:
                length[idx][jdx] = max(length[idx - 1][jdx],
                                       length[idx][jdx - 1])
    return length[len1 - 1][len2 - 1]


def word_token(data):
    """
    data: string
    return: words in the string
    """
    n_char = len(data)

    sdx, edx = 0, 0
    words = []
    for jdx in range(n_char):
        if jdx == 0 and data[0].isalpha():
            sdx = 0
        elif not data[jdx - 1].isalpha() and data[jdx].isalpha():
            sdx = jdx

        if data[jdx - 1].isalpha() and not data[jdx].isalpha():
            edx = jdx
            words.append(data[sdx:edx])

    if edx != n_char - 1 and data[n_char - 1].isalpha():
        words.append(data[sdx:n_char])

    return words


def palindrome(word):
    return all(word[idx] == word[len(word) - idx - 1]
               for idx in range(len(word) // 2))


def all_substrings(word):
    substrings = [word[sdx:edx]
                  for sdx in range(len(word))
                  for edx in range(sdx + 1, len(word) + 1)
                  ]
    return substrings


def int_to_str(n, base):
    """ uva 389 """
    symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output = []
    while n > 0:
        output.append(symbols[n % base])
        n //= base
    return "".join(reversed(output))


def is_square(positive_int):
    """
    uva 636
    Babylonian algorithm
    https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    """
    x = positive_int // 2
    seen = set([x])
    while x * x != positive_int:
        x = (x + (positive_int // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def is_square2(positive_int):
    from math import sqrt, floor
    x = positive_int
    return x == int(floor(sqrt(x) + 0.5) ** 2)


def int_from_base(val, base):
    """ val: string """
    res = int(val[0])
    for v in val[1:]:
        res = res * base + int(v)
    return res


def infix_to_postfix(infix_expr):
    """
    uva 727
    infix_expr: string or list """
    prec = {}
    # priority
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stack = []
    postfix_expr = []

    for token in infix_expr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix_expr.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                # pop element until match brace
                postfix_expr.append(top_token)
                top_token = stack.pop()
        else:
            # the token is an operator
            while stack and prec[stack[-1]] >= prec[token]:
                postfix_expr.append(stack.pop())
            stack.append(token)

    while stack:
        postfix_expr.append(stack.pop())
    return "".join(postfix_expr)
