# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/128/12895.pdf
"""

def is_Armstrong(val):

    exp = 1
    digits = [ord(c)-ord('0') for c in str(val)]
    while 1:
        digit_exp_sum = sum(map(lambda x:x**exp, digits))
        if digit_exp_sum == val:
            return True
        elif digit_exp_sum > val:
            return False
        else:
            exp += 1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())  
        if not is_Armstrong(N):
            print ("Not ", end="")
        print ("Armstrong")

if __name__ == '__main__':
    main()