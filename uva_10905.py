# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/109/10905.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10905.htm
"""

import functools

def concat_function(val1, val2):
    """
    comparing the concatenation between (val1 + val2) and (val2 + val1)
    """
    t1, t2 = "".join([val1, val2]), "".join([val2, val1])
    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1
    else:
        return 0

def main():
    while 1:
        N = int(input())
        if N == 0:
            break
        data = input().split()
        val = sorted(data, key=functools.cmp_to_key(concat_function),
                      reverse=True)
        print ("".join(val))

if __name__ == '__main__':
    main()
