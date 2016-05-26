# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

http://luckycat.kshs.kh.edu.tw/homework/q11956.htm
http://luckycat.kshs.kh.edu.tw/homework/q11956.htm
"""


def main():
    T = int(input())
    for tdx in range(T):
        memory = [0] * 100
        ptr = 0
        cmds = input().strip()
        for cmd in cmds:
            if cmd == '>':
                ptr = (ptr + 1) % 100
            elif cmd == '<':
                ptr = (ptr - 1) % 100
            elif cmd == '+':
                memory[ptr] = (memory[ptr] + 1) % 256
            elif cmd == '-':
                memory[ptr] = (memory[ptr] - 1) % 256

        print("Case {}: {}".format(tdx + 1,
                                   " ".join(
                                       ["{:02X}".format(v) for v in memory])))


if __name__ == '__main__':
    main()
