# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/116/11650.pdf
"""


def main():
    n_case = int(input())
    for _ in range(n_case):
        m_hour, m_minute = list(map(int, input().split(':')))
        r_hour = 11 - m_hour + int(m_minute == 0)
        r_hour += 12 if r_hour <= 0 else 0
        r_minute = 60 - m_minute if m_minute != 0 else m_minute
        print("{:02d}:{:02d}".format(r_hour, r_minute))


if __name__ == '__main__':
    main()
