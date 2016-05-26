# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10919.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10919.htm
"""


def main():
    while 1:
        record = input().split()
        if record[0] == '0':
            break
        n_chosen, n_category = list(map(int, record))

        # One or more lines follow containing k 4-digit integers follow
        chosen = []
        for _ in range(n_chosen):
            chosen.extend(input().split())
            if len(chosen) >= n_chosen:
                break

        satisfied = True
        for _ in range(n_category):
            data = input().split()
            n_course = int(data[0])
            n_required = int(data[1])
            courses = frozenset(data[2:])

            cnt = 0
            for c in chosen:
                if c in courses:
                    cnt += 1
                if cnt >= n_required:
                    break
            if cnt < n_required:
                satisfied = False

        print("yes" if satisfied else "no")


if __name__ == '__main__':
    main()
