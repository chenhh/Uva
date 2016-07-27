# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

123 Searching Quickly

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/1/123.pdf
"""

import sys
from collections import deque


def main():
    ignores = []
    stack = deque()
    stack_append = stack.append
    stack_clear = stack.clear
    kwic = []
    kwic_append = kwic.append
    recs = iter(sys.stdin.readlines())

    is_ignore = True
    while True:
        try:
            data = next(recs).strip('\n')
            if data == '::':
                is_ignore = False
                ignores = frozenset(ignores)
                continue

            if is_ignore:
                # Each of the words to ignore appears in lower-case letters
                ignores.append(data)
            else:
                # original title
                title = data.lower()

                stack_clear()
                for idx, ch in enumerate(title):
                    if ch.isalpha():
                        stack_append(idx)
                    elif stack:
                        sdx = stack[0]
                        edx = stack[-1] + 1
                        stack_clear()
                        key = title[sdx:edx]
                        if key not in ignores:
                            kwic_append((key, "".join((title[0:sdx],
                                                       title[sdx:edx].upper(),
                                                       title[edx:]))))
                if stack:
                    sdx = stack[0]
                    edx = stack[-1] + 1
                    stack_clear()
                    key = title[sdx:edx]
                    if key not in ignores:
                        kwic_append((key, "".join((title[0:sdx],
                                                   title[sdx:edx].upper(),
                                                   title[edx:]))))


        except (StopIteration):
            # process
            kwic.sort(key=lambda x: x[0])
            for _, val in kwic:
                print(val)

            break


if __name__ == '__main__':
    main()
