# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q12149.htm
math

1^2 + 2^2 + 3^2 + \dots + n^ = n*(n+1)*(2n+1)/6
"""
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print (n*(n+1)*(2*n+1)//6)
      
if __name__ == '__main__':
    main()