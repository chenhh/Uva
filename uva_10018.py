# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10018.htm
"""

def is_palindrome(data):
    length = len(data)
    if length % 2 == 0:
        edx = length // 2
        sdx = edx
    else:
        edx = (length +1) // 2
        sdx = edx -1
    return data[:edx] == data[sdx:][::-1]

def main():
    N = int(input())
    for _ in range(N):
        pos = input()
        cnt = 0
        for idx in range(1, 1001):
            num1 = int(pos)
            num2 = int(pos[::-1])
            pos = str(num1 + num2)
            # print (pos)
            if is_palindrome(pos):
                cnt = idx
                break
        print ("{} {}".format(cnt, pos))

if __name__ == '__main__':
    main()