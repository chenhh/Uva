# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: working
difficulty: 2

https://uva.onlinejudge.org/external/101/10142.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10142.htm

If no candidate receives more than 50%, all candidates tied for the
lowest number of votes are eliminated.

Ballots ranking these candidates first are recounted in favour of their
highest ranked candidate who has not been eliminated.
"""

import sys
from collections import deque


def winner(all_votes, n_candidate):
    """ n_candidate == n_col of all_votes """
    n_voter = len(all_votes)
    # more than 50%
    threshold = n_voter // 2

    for round in range(n_candidate):
        get_vote = {idx + 1: 0 for idx in range(n_candidate)}
        for data in all_votes:
            get_vote[data[0]] += 1


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    _ = next(recs)

    for _ in range(n_case):
        n_candidate = int(next(recs))
        names = [next(recs).strip() for _ in range(n_candidate)]
        all_votes = []
        while 1:
            try:
                votes = next(recs).strip()
                if votes:
                    all_votes.append(deque(map(int, votes.split())))
                else:
                    print(all_votes)

                    break
            except (StopIteration):
                break


if __name__ == '__main__':
    main()
