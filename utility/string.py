# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""


def quick_lis(seqs):
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


def dp_lis(box_items, n_box):
    """
    uva 103
    dynamic programming
    lis(n) = max (lis(i) + 1: if s[i] <s[n])
    """

    def cmp_dominated(box_item1, box_item2):
        """
        box_item: key, values

        return a negative value for less-than,
        return zero if they are equal, or
        return a positive value for greater-than.
        """
        _, box1 = box_item1
        _, box2 = box_item2
        n_dim = len(box1)

        for idx in range(n_dim):
            if box1[idx] >= box2[idx]:
                # box2 does not dominating box1, equal
                return 0
        # box2 dominating box1
        return 1

    keys, boxes = zip(*box_items)

    # each element is an lis of length 1
    len_lis = [1] * n_box
    prev = [-1] * n_box

    for idx in range(n_box):
        for jdx in range(idx + 1, n_box):
            if cmp_dominated(box_items[idx], box_items[jdx]):
                # jdx dominating idx
                if len_lis[idx] + 1 > len_lis[jdx]:
                    # jdx item is behind the idx item
                    len_lis[jdx] = len_lis[idx] + 1
                    prev[jdx] = idx
    # print (len_lis)
    # print (prev)
    max_len_lis = max(len_lis)

    # traceback
    curr = 0
    for idx in range(n_box):
        if len_lis[idx] == max_len_lis:
            curr = idx
            break

    ans = []
    while curr != -1:
        ans.append(keys[curr])
        curr = prev[curr]

    return (max_len_lis, " ".join(map(str, ans[::-1])))




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

    lcs_length = length[len1 - 1][len2 - 1]

    # traceback
    idx = len1 - 1
    jdx = len2 - 1
    lcs_words = [[] for _ in range(lcs_length)]
    kdx = lcs_length - 1
    while kdx >= 0:
        if line1[idx] == line2[jdx]:
            # match
            lcs_words[kdx] = line1[idx]
            kdx -= 1
            idx -= 1
            jdx -= 1
        else:
            if length[idx][jdx - 1] > length[idx - 1][jdx]:
                # the lcs values comes from left
                jdx -= 1
            else:
                # the lcs values comes from upper
                idx -= 1

    return lcs_length, lcs_words


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
    infix_expr: string or list
    """
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


def longest_palindrome(word, sdx, edx, table):
    """ uva 11151 """
    if sdx == edx:
        # the empty string is a palindrome
        return 1

    if sdx == edx - 1:
        if word[sdx] == word[edx]:
            return 2
        else:
            return 1

    if table[sdx][edx] != -1:
        # checked
        return table[sdx][edx]

    if word[sdx] == word[edx]:
        table[sdx][edx] = 2 + longest_palindrome(word, sdx + 1, edx - 1, table)
    else:
        table[sdx][edx] = max(longest_palindrome(word, sdx, edx - 1, table),
                              longest_palindrome(word, sdx + 1, edx, table))
    return table[sdx][edx]
