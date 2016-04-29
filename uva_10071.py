# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10071.htm
"""

def main():
    while True:
        try:
            strs = input()
            v, t = [int(v) for v in strs.split()]
            print(2*v*t)

        except (EOFError):
            break

if __name__ == '__main__':
    main()