# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 2

https://uva.onlinejudge.org/external/119/11995.pdf
"""

import heapq
from collections import deque


def main():
    while 1:
        try:
            n_cmd = int(input())
            stack, queue, min_heap = [], deque([]), []
            vote = [1, 1, 1]
            for _ in range(n_cmd):
                cmd, value = list(map(int, input().split()))
                if cmd == 1:
                    stack.append(value)
                    queue.append(value)
                    heapq.heappush(min_heap, -value)

                elif cmd == 2:
                    if len(stack) == 0 or value != stack.pop():
                        vote[0] = 0
                    if len(queue) == 0 or value != queue.popleft():
                        vote[1] = 0
                    if len(min_heap) == 0 or value != -heapq.heappop(min_heap):
                        vote[2] = 0

            ans = sum(vote)
            if ans == 0:
                print('impossible')
            elif ans >= 2:
                print('not sure')
            else:
                if vote[0]:
                    print('stack')
                elif vote[1]:
                    print('queue')
                else:
                    print('priority queue')

        except (EOFError):
            break


if __name__ == '__main__':
    main()
