# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/124/12403.pdf
"""

def main():
    T = int(input())

    account = 0
    for _ in range(T):
        op = input().strip()

        if op == "report":
            print (account)
        else:
            account += int(op.split()[1])

if __name__ == '__main__':
    main()