# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/727.pdf
infix to postfix
"""

import sys
from collections import deque


def infix_to_postfix(infix_expr):
    """ infix_expr: string or list """
    prec = {}
    # priority
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    stack = deque()
    postfix_expr = deque()

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


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for tdx in range(n_case):
        try:
            infix_expr = []
            while True:
                data = next(recs).strip()
                if data:
                    infix_expr.append(data)
                else:
                    raise GeneratorExit

        except (StopIteration, GeneratorExit):
            if infix_expr:
                if tdx:
                    print()
                print(infix_to_postfix(infix_expr))


if __name__ == '__main__':
    main()
