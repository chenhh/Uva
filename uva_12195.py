# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q12195.htm
"""


def main():
    symbol = {'W': 1, 'H': 1 / 2, 'Q': 1 / 4, 'E': 1 / 8,
              'S': 1 / 16, 'T': 1 / 32, 'X': 1 / 64
              }
    eps = 1e-8
    while True:
        data = input()
        if data == "*":
            break
        comps = data[1:-1].split('/')
        cnt = 0
        for comp in comps:
            value = 0
            for a in comp:
                value += symbol[a]
            if (abs(value - 1)<=eps):
                cnt += 1
        print (cnt)

if __name__ == '__main__':
    main()
