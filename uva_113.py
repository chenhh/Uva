# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q113.htm
"""
import math
def main():
    while True:
        try:
            n = int(input())
            p = int(input())
            #k**n = p
            print (round(pow(p, 1/n)))

        except (EOFError):
            break

if __name__ == '__main__':
    main()