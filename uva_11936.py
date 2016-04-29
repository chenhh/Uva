# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11936.htm
"""
def main():
    N = int(input())
    for _ in range(N):
        strs = input()
        edges = sorted([int(v) for v in strs.split()])
        sol = True
        if edges[0] <= 0 or edges[2] <=0:
            sol = False
        elif edges[0] + edges[1] <= edges[2]:
            sol = False
    
        print ("OK" if sol else "Wrong!!")
        
if __name__ == '__main__':
    main()