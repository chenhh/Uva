# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: working
difficulty: 1
Q12459 - Bees' ancestors
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=279&page=show_problem&problem=3890
http://luckycat.kshs.kh.edu.tw/homework/q12459.htm

a female bee has two parents (one father and one mother)
a male bee has a mother but no father.

assuming male:0, female: 1
the parent of male: 0 -> 1
the parents of female: 1->01
gen: 1    2     3      4        5
0 -> 1 -> 01 -> 101 -> 01101 -> 10101101
     1     2    3      5        8

the number of parents in ith generation is the ith Fibonacci number.
"""

def main():
    fib = [1,1]
    for idx in range(2, 81):
        fib.append(fib[idx-1] + fib[idx-2])

    while 1:
        gen = int(input())
        if gen == 0:
            break
        print (fib[gen])

if __name__ == '__main__':
    main()