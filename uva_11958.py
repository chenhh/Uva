# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/119/11958.pdf
"""


def main():
    n_case = int(input())
    for tdx in range(1, n_case + 1):
        n_bus, curr_time = input().split()
        curr_hour, curr_min = list(map(int, curr_time.split(':')))
        base_min = curr_hour * 60 + curr_min

        min_arrival = 3600
        for _ in range(int(n_bus)):
            arrive_time, travel = input().split()
            arrive_hour, arrive_min = list(map(int, arrive_time.split(':')))
            arrive_base_min = arrive_hour * 60 + arrive_min
            if arrive_base_min < base_min:
                # the bus arrival after 24 hours
                arrive_base_min += 1440
            arrive_base_min += int(travel)
            if arrive_base_min < min_arrival:
                min_arrival = arrive_base_min

        print("Case {}: {}".format(tdx, min_arrival - base_min))


if __name__ == '__main__':
    main()
