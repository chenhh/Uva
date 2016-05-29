# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1

https://uva.onlinejudge.org/external/1/151.pdf
http://luckycat.kshs.kh.edu.tw/homework/q151.htm
"""


def link_list(N, m):
    """
    using array to implement one direction link list
    the list start from 1,2,...,N
    find m such that 13th element is the last-chosen element.
    """
    # neglect the first (0th) element
    nexts = list(range(1, N + 1))
    nexts[-1] = 1
    head, prev, last = 1, N - 1, 0

    for idx in range(1, N + 1):
        for jdx in range(m - 1):
            # move to next element
            prev = head
            head = nexts[head]
        # print (last+1)
        last = head
        # update link list, skip the last element
        nexts[prev] = nexts[head]
        head = nexts[head]
    return True if last == 12 else False


def main():
    ans = [0] * 100
    for idx in range(13, 100):
        count = 1
        while not link_list(idx, count):
            count += 1
        ans[idx] = count
    while 1:
        # 13 <= N < 100
        N = int(input())
        if not N:
            break
        print(ans[N])


if __name__ == '__main__':
    main()
