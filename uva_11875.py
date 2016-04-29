# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11875.htm
median
"""

def main():
    n = int(input())
    for idx in range(n):
        strs = input()
        values = [int(v) for v in strs.split()]
        n_number, ages = values[0], values[1:]
        print ("Case {}: {}".format(idx+1, ages[(n_number-1)//2]))
        
if __name__ == '__main__':
    main()