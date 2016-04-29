# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=25&page=show_problem&problem=2349
http://luckycat.kshs.kh.edu.tw/homework/q11364.htm
sort and median
"""

def main():
    t = input()
    t = int(t)
    for cnt in range(t):
        v1 = input()
        v2 = input()
        
        n_shop = int(v1)
        addrs = sorted(int(v) for v in  v2.split())
        n_addrs = len(addrs)
        if n_addrs % 2 == 1:
            median = addrs[(n_addrs-1)//2]
        else:
            median = (addrs[n_addrs//2] + addrs[n_addrs//2 - 1])//2
     
        dist = sum(abs(addrs[idx] - addrs[idx-1]) for idx in range(1, n_addrs))
        dist += (median - addrs[0])
        dist += (addrs[n_addrs-1] - median)
        print (dist)
        
if __name__ == '__main__':
    main()