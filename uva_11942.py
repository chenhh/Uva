# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11942.htm
"""

def main():
    N = int(input())
    print ("Lumberjacks:")
    for _ in range(N):
        data = input()
        values = [int(v) for v in data.split()]
        n_value = len(values)
        
        inc = True
        for idx in range(1, n_value):
            if values[idx] <= values[idx - 1]:
                inc = False
                break
                
        dec = True
        for idx in range(n_value-2, 0, -1):
            if values[idx+1] >= values[idx]:
                dec = False
                break
        print ("Ordered" if any((inc, dec)) else "Unordered")
        
if __name__ == '__main__':
    main()