# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10107.htm
median
"""
import bisect

def main():
    arr = []
    arr_len = 0
    while True:
        try:
            val = int(input())
            
            # insert point
            bisect.insort_left(arr, val)
            arr_len += 1
            if arr_len % 2 == 1:
                print (arr[(arr_len-1)//2])
            else:
                print ((arr[arr_len//2]+arr[arr_len//2 -1])//2)
            
        except (EOFError):
            break
    
if __name__ == '__main__':
    main()