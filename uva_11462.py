# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11462.htm
"""

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        data = input()
        ages = sorted(int(v) for v in data.split())
        print (" ".join(str(v) for v in ages))
        
if __name__ == '__main__':
    main()