# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11764.htm
"""

def main():
    T = int(input())
    for idx in range(T):
        N = int(input())
        strs = input()
        walls = [int(v) for v in strs.split()]
        
        inc, dec =0, 0
        for pos in range(1, N):
            if walls[pos] > walls[pos-1]:
                inc += 1
            elif walls[pos] < walls[pos-1]:
                dec += 1
        print ("Case {}: {} {}".format(idx+1, inc, dec))
   
if __name__ == '__main__':
    main()