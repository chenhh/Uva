# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=19&page=show_problem&problem=1724
http://luckycat.kshs.kh.edu.tw/homework/q10783.htm
Arithmetic progression
"""

def main():
    T = input()
    T = int(T)
    
    for idx in range(T):
        s_a = input()
        s_b = input()
        a, b, = int(s_a), int(s_b)
        sdx = a + 1 if a % 2 == 0 else a
        edx = b - 1 if b % 2 == 0 else b
           
        n = (edx-sdx)//2 + 1
        s = n*(sdx+edx) // 2
        print ("Case {}: {}".format(idx+1, s))

if __name__ == '__main__':
    main()