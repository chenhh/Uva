# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11984.htm
math

"""
def main():
    n = int(input())
    for idx in range(n):
        strs = input()
        C, d = [int(v) for v in strs.split()]
        F = (9*C)/5 + 32
        F += d
        NC = (F-32)*5/9
        print ("Case {}: {:.2f}".format(idx+1, NC))
      
if __name__ == '__main__':
    main()