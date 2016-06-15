# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/110/11057.pdf
"""

import bisect
import sys


def solve(n_book, books, money):
    half = money // 2
    edx = bisect.bisect_right(books, half)
    if books[edx - 1] == half:
        edx -= 1
    sdx = max(edx - 1, 0)
    curr = books[sdx] + books[edx]
    # print (curr, sdx, edx)
    while curr != money and sdx >= 0 and edx < n_book:
        if curr < money:
            edx += 1
        elif curr > money:
            sdx -= 1
        curr = books[sdx] + books[edx]
        # print(curr, sdx, edx)
    print("Peter should buy books whose prices are {} and {}.".format(
        books[sdx], books[edx]))
    print()


def main():
    recs = iter(sys.stdin.readlines())

    while 1:
        try:
            n_book = int(next(recs))
            books = sorted(list(map(int, next(recs).split())))
            money = int(next(recs))
            line = next(recs).strip()
            if not line:
                solve(n_book, books, money)
                books.clear()

        except (StopIteration):
            if books:
                solve(n_book, books, money)
            break


if __name__ == '__main__':
    main()
