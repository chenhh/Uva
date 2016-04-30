# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11219.htm
"""
from datetime import date

def main():
    T = int(input())
    for tdx in range(T):
        _ = input()
        curr = date(*list(map(int, input().split('/')))[::-1])
        birth = date(*list(map(int, input().split('/')))[::-1])
        
        if birth > curr:
            print ("Case #{}: Invalid birth date".format(tdx+1))
            continue
            
        year_diff = curr.year - birth.year
        if curr.month < birth.month:
            year_diff -= 1
        elif curr.month == birth.month and curr.day < birth.day:
            year_diff -= 1
        
        if year_diff > 130:
            print ("Case #{}: Check birth date".format(tdx+1))
        else:
            print ("Case #{}: {}".format(tdx+1, year_diff))
              
if __name__ == '__main__':
    main()