# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10055.htm
"""

def main():
    while True:
        try:
            val, val2 = list(map(int, input().split()))
            print (abs(val-val2))
        except (EOFError):
            break

if __name__ == '__main__':
    main()