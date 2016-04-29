# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3912
http://luckycat.kshs.kh.edu.tw/homework/q12468.htm
"""

def main():
    while True:
        strs = input()
        src, tgt = [int(v) for v in strs.split()]
        if src == -1 and tgt == -1:
            break
     
        c1 = abs(src - tgt)
        c2 = (99 - max(src,tgt)) + min(src, tgt) + 1
        print (min(c1, c2))

if __name__ == '__main__':
    main()