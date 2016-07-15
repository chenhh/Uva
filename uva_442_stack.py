# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/4/442.pdf
http://luckycat.kshs.kh.edu.tw/homework/q442.htm
"""

import sys
from collections import deque


def main():
    recs = iter(sys.stdin.readlines())
    n_mtx = int(next(recs))

    mtx_dict = {}
    for _ in range(n_mtx):
        name, n_row, n_col = next(recs).split()
        mtx_dict[name] = (int(n_row), int(n_col))

    mtx_name = mtx_dict.keys()
    queue = deque()
    queue_pop = queue.pop
    queue_appendleft = queue.appendleft
    queue_clear = queue.clear
    mul = deque()
    mul_clear = mul.clear
    mul_append = mul.append
    mul_pop = mul.pop

    while True:
        cnt = 0
        is_legal = True
        try:
            eq = next(recs).strip()
            mul_clear()

            for token in eq:
                if not is_legal:
                    break

                if token == '(':
                    # left boundary
                    mul_append(token)

                elif token == ')':
                    # right boundary, pop the item to the left boundary
                    top_token = mul_pop()
                    queue_clear()
                    while top_token != '(':
                        # backtrack
                        queue_appendleft(top_token)
                        top_token = mul_pop()

                    # check the matrix size
                    if len(queue) == 1:
                        mtx_shape = queue[0]
                    else:
                        for idx in range(1, len(queue)):
                            prev = queue[idx - 1]
                            curr = queue[idx]
                            cnt += prev[0] * prev[1] * curr[1]
                            if prev[1] != curr[0]:
                                is_legal = False
                                break
                        mtx_shape = (queue[0][0], queue[-1][1])

                    mul_append(mtx_shape)
                else:
                    # a matrix
                    mul_append(mtx_dict[token])

            if not is_legal:
                # illegal in pre-stage
                print('error')
            else:
                if len(mul) > 1:
                    for idx in range(1, len(mul)):
                        prev = mul[idx - 1]
                        curr = mul[idx]
                        cnt += prev[0] * prev[1] * curr[1]
                        if prev[1] != curr[0]:
                            is_legal = False
                            break
                if not is_legal:
                    print("error")
                else:
                    print(cnt)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
