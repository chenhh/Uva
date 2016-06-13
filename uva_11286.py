# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/112/11286.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11286.htm
https://www.ptt.cc/bbs/C_and_CPP/M.1324909774.A.32D.html
"""

from collections import defaultdict


def main():
    while 1:
        n_student = int(input())
        if not n_student:
            break

        popularity = defaultdict(int)
        for _ in range(n_student):
            courses = "".join(str(v) for v in
                              sorted(list(map(int, input().split()))))
            popularity[courses] += 1

        # print (popularity)
        # if there is only one most popular course, output the number of it
        # if there are multiple most popular course, output the total numbers.
        most_course, n_num = 0, 0
        for _, num in popularity.items():
            if num > most_course:
                # current course is the most popular
                most_course = num
                ans = 0
            if num == most_course:
                ans += num

        print(ans)


if __name__ == '__main__':
    main()
