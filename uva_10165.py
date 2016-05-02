# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1106
par.cse.nsysu.edu.tw/~advprog/.../10165.doc

analysis the endgame: (safe, and unsafe endgame)
If the number of stone in a pile is even, then I must win.
If there are stones in different piles, do xor operations (enemy and I both act at least once) in all piles. 
If the value still be even, then I must win.
"""

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        piles = list(map(int, input().split()))
        ans = 0
        for pile in piles:
            ans ^= pile
        print ("Yes" if ans else "No")
        
if __name__ == '__main__':
    main()
