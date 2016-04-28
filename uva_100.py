# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36
http://acm-solution.blogspot.tw/2010/08/acm-uva-100-3n-1-problem.html
min: 1, maximum: 1,000,000
"""
from array import array

def cycle_length_orig(n):
    """
    n: positive integer  
    TLE　version
    """
    cnt = 1
    while (n != 1):
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n /= 2
        cnt += 1
    return cnt

MAX = 1000001
cache = [0] * MAX

def cycle_length(value):
    """
    n: positive integer  
    cache computed value
    """
    if value < MAX and cache[value] != 0:
        return cache[value]
    if value == 1:
        return 1
    elif value == 2:
        return 2
    elif value % 2 == 1:
        if value < MAX:
            cache[value] = 2 + cycle_length(int( (3*value + 1)/2 ))
            return cache[value]
        else:
            return 2 + cycle_length(int( (3*value + 1)/2 ))
    else:
        if value < MAX:
            cache[value] = 1+ cycle_length(int(value/2))
            return cache[value]
        else:
            return 1+ cycle_length(int(value/2))

def main():
    while True:
        try:
            data = input()
            v1, v2 = map(lambda x: int(x), data.split())
            out = 0
            for v in range(min(v1, v2), max(v1, v2)+1):
                sol = cycle_length(v)
                if  sol > out:
                    out = sol
            print ("{} {} {}".format(v1, v2, out))
        except (EOFError):
            break

if __name__ == '__main__':
    main()
