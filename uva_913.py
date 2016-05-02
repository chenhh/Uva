# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q913.htm

The number of element of k-th row is (2k-1).
The total number of element from 1st to kth row is (1+2k-1)*k/2=k^2.
The value of last element in the k-th row is 1+(k^2-1)*2

The row which contains N (odd) elements is the (N+1)/2 th row.
The value of last element of  (N+1)/2 row is (N^2+2N+1)/2 -1
the solution sum of a+b+c
a = (N^2+2N+1)/2 -1
b = a-2
c = a-4
therefore a+b+c = (3*N^2+6*N+3)/2-9
"""
def main():
    while True:
        try:
            N = int(input())
            print ((3*N**2+6*N+3)//2 - 9)
        except (EOFError):
            break

if __name__ == '__main__':
    main()