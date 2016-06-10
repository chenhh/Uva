# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/103/10374.pdf

riding: https://en.wikipedia.org/wiki/Riding_(country_subdivision)
"""

from collections import Counter


def main():
    n_case = int(input())

    for tdx in range(n_case):
        name_party = {}
        while 1:
            data = input().strip()
            if len(data):
                n_candidate = int(data)
                break
        for _ in range(n_candidate):
            # No candidate name is repeated and no party name is repeated
            name = input().strip()
            party = input().strip()
            name_party[name] = party

        name_set = frozenset(name_party.keys())
        n_vote = int(input())
        votes = []
        for _ in range(n_vote):
            # Any names not in the list of candidates should be ignored.
            vote = input().strip()
            if vote in name_set:
                votes.append(vote)

        if tdx:
            print()

        if len(votes) == 0:
            # no valid votes
            print('tie')
        elif len(votes) == 1:
            # only one valid vote
            print(name_party[votes[0]])
        else:
            # at least two valid votes
            votes_cnt = Counter(votes)
            # print (votes_cnt)
            max_name, max_cnt = votes_cnt.most_common(1)[0]
            tie = False
            for name, cnt in votes_cnt.items():
                if cnt == max_cnt and name != max_name:
                    tie = True
                    break
            if tie:
                print('tie')
            else:
                print(name_party[max_name])


if __name__ == '__main__':
    main()
