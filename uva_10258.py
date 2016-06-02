# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status:
difficulty: 1

https://uva.onlinejudge.org/external/102/10258.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10258.htm
"""


def main():
    n_case = int(input())
    _ = input()

    for cdx in range(n_case):
        # the dict store a list, and each element of of the list is a
        # nine-dimensional value
        contestants = {}
        while 1:
            try:
                record = input().split()
                if not len(record):
                    break
                contestant_id = int(record[0])
                problem_id = int(record[1]) - 1
                sol_time = int(record[2])
                state = record[3]

                if contestant_id not in contestants.keys():
                    contestants[contestant_id] = [None] * 9

                if contestants[contestant_id][problem_id] is None:
                    # the problem does not solve before
                    if state in ('R', 'U', 'E'):
                        contestants[contestant_id][problem_id] = 0
                    elif state == 'I':
                        # WA
                        contestants[contestant_id][problem_id] = -1
                    elif state == 'C':
                        # AC
                        contestants[contestant_id][problem_id] = sol_time
                elif contestants[contestant_id][problem_id] > 0:
                    # the problem is solved before
                    continue
                elif contestants[contestant_id][problem_id] <= 0:
                    # the problem does not solve correctly
                    if state == 'I':
                        # WA
                        contestants[contestant_id][problem_id] -= 1
                    elif state == 'C':
                        # AC
                        contestants[contestant_id][problem_id] = (
                            abs(contestants[contestant_id][problem_id]) * 20 +
                            sol_time
                        )

            except (EOFError):
                break

        # statistics
        rank = []
        for k, times in contestants.items():
            cnt, score = 0, 0
            for t in times:
                if t and t > 0:
                    cnt += 1
                    score += t
            rank.append((k, cnt, score))

        # sort by (1st: cnt (descending), 2: time (ascending), 3: user_id (as)
        rank.sort(key=lambda x: (-x[1], x[2], x[0]))

        if cdx:
            print()

        # print, sorted by score (descending)
        for uid, cnt, score in rank:
            print("{} {} {}".format(uid, cnt, score))


if __name__ == '__main__':
    main()
