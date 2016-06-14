# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/485.pdf
When any number in the triangle is exceeds or equals 10**60, your 
program should finish printing the current row and exit.
"""
  
def main():
    THRESHOLD =10**60
    r1, r2 = [1], [1, 1]
    while 1:
        print(" ".join(map(str, r1)))
        if max(r1) >= THRESHOLD:
            break
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
       
if __name__ == '__main__':
    main()