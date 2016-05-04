# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2827
"""

def main():
    T = int(input())

    for idx in range(T):
        salary = map(int, input().split())
        print ("Case {}: {}".format(idx+1, sorted(salary)[1]))

if __name__ == '__main__':
    main()