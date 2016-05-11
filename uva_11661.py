# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11661.htm
https://uva.onlinejudge.org/external/116/11661.pdf
to find the shortest distance between a restaurant and a drugstore
"""


def main():
    while 1:
        road_len = int(input())
        if road_len == 0:
            break

        road = input().strip()
        dist = road_len

        if 'Z' in road:
            dist = 0
        else:
            # greedy update distance
            restaurant, drugstore = 0, 0
            for idx, v in enumerate(road):
                if v == 'R':
                    restaurant = idx+1
                elif v == 'D':
                    drugstore = idx+1

                if restaurant  and drugstore:
                    curr_dist = abs(restaurant - drugstore)
                    if curr_dist < dist:
                        dist = curr_dist

        print (dist)

if __name__ == '__main__':
    main()