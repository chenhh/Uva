# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11879.htm
"""

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print (1 if n % 17 == 0 else 0)
        
if __name__ == '__main__':
    main()