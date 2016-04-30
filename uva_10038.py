# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10038.htm
"""

def main():
    while True:
        try:
            data = list(map(int, input().split()))
            n = data[0]
            arr = data[1:]
            diff =set([abs(arr[idx] - arr[idx-1]) for idx in range(1, n)])
            jolly = set(list(range(1,n)))
            print ( "Jolly" if diff == jolly else "Not jolly")

        except (EOFError):
            break

if __name__ == '__main__':
    main()
