# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10929.htm
"""

def main():
    while True:
        val = input()
        N = int(val)
        if N == 0:
            break
        sol = True if N % 11 == 0 else False
        if sol:
            print ("{} is a multiple of 11.".format(val.strip()))
        else:
            print ("{} is not a multiple of 11.".format(val.strip()))
  
if __name__ == '__main__':
    main()