# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=602&page=show_problem&problem=4280
http://luckycat.kshs.kh.edu.tw/homework/q12602.htm
"""

def decimal(p1):
    value = 0
    for idx, digit in enumerate(p1):
        value += (ord(digit.upper()) - ord('A'))*(26**(2-idx))
    return value

def main():
    n_data = int(input())
    for _ in range(n_data):
        plate = input()
        p1, p2 = plate.split('-')
        
        if abs(decimal(p1) - int(p2)) <= 100:
            print ("nice")
        else:
            print ("not nice")
        
if __name__ == '__main__':
    main()