# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/116/11683.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11683.htm
count the disconnect interval in each height
"""


def laser_count(height, length, shapes):
    """ O(n^2), correct but TLE """
    # shape: length
    count = 0
    for level in reversed(range(1, height + 1)):
        # product shape of each level
        blocks = [True] * length
        for idx, shape in enumerate(shapes):
            if shape >= level:
                blocks[idx] = False
        # print (level, blocks)
        blocks.append(False)
        for jdx in range(length):
            if blocks[jdx] == True and blocks[jdx + 1] == False:
                count += 1
    return count


def laser_count2(height, length, shapes):
    """ O(n) version """
    count = height - shapes[0]
    for idx in range(1, length):
        if shapes[idx] < shapes[idx - 1]:
            count += (shapes[idx - 1] - shapes[idx])
    return count


def main():
    while 1:
        # 1 <= height, length <= 10000
        height, length = list(map(int, input().split()))
        if height == 0 and length == 0:
            break
        # shape: length
        shapes = list(map(int, input().split()))
        # ans = laser_count(height, length, shapes)
        ans2 = laser_count2(height, length, shapes)
        print(ans2)


if __name__ == '__main__':
    main()
