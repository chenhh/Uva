# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

http://luckycat.kshs.kh.edu.tw/homework/q488.htm
"""

def wave(A):
    msg = []
    for idx in range(1, A+1):
        msg.append(str(idx)*(idx))

    for idx in range(A-1, 0, -1):
        msg.append(str(idx)*(idx))
    return msg

def main():
    n = int(input())

    for idx in range(n):
        _ = input()
        A = int(input())
        F = int(input())

        for jdx in range(F):
            msg = wave(A)
            print("\n".join(msg))
            if idx != n-1 or jdx != F-1:
                print ()

if __name__ == '__main__':
    main()