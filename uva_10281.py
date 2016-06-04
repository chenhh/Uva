# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/102/10281.pdf

Elapsed times are given in non-decreasing order and there is at most one
speed change at any given time.
"""


def main():
    curr_time, prev_time, curr_speed = 0, 0, 0
    dist = 0
    while 1:
        try:
            data = input().split()
            # Elapsed times are given in non-decreasing order
            hh, mm, ss = list(map(int, data[0].split(':')))
            curr_time = hh * 3600 + mm * 60 + ss
            time_shift = curr_time - prev_time
            dist += curr_speed * time_shift / 3600

            if len(data) == 2:
                # current time and speed
                curr_speed = int(data[1])
            else:
                # query
                # print (prev_time, curr_time)
                print("{:02d}:{:02d}:{:02d} {:.2f} km".format(
                    hh, mm, ss, dist))

            # update time
            prev_time = curr_time

        except (EOFError):
            break


if __name__ == '__main__':
    main()
