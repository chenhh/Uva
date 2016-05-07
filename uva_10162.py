# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/101/10162.pdf

S = 1**1 + 2**2 + 3**3 + ... + n**n
to get the last digit of S

n=1, S=1, answer: 1
n=2, S=1+4=5, answer: 5
n=3, S=1+4+27=32, answer: 2

base: b
decimal digit of exponent d is even
decimal digit of exponent d is odd

the digit number when
--------------------------
(b, d is even, d is odd)
0,  0,  0 (10^20 10^30 = {\d*}0 )
1,  1,  1 (1^1 21^21={\d*}1     11^11 31^31={\d*}1)
2,  4,  6 (2^2 22^22={\d*}4     12^12 32^32={\d*}6)
3,  7,  3 (3^3 23^23={\d*}7     13^13 33^33={\d*}3)
4,  6,  6 (4^4 24^24={\d*}6     14^14 34^34={\d*}6)
5,  5,  5 (5^5 25^25={\d*}5     15^15 35^35={\d*}5)
6,  6,  6 (6^6 26^26={\d*}6     16^16 36^36={\d*}6)
7,  3,  7 (7^7 27^27={\d*}3     17^17 37^37={\d*}7)
8,  6,  4 (8^8 28^28={\d*}6     18^18 38^38={\d*}4)
9,  9,  9 (9^9 29^29={\d*}9     19^19 39^39={\d*}9)
"""

def main():
    digits = [
        [0, 1, 4, 7, 6, 5, 6, 3, 6, 9],
        [0, 1, 6, 3, 6, 5, 6, 7, 4, 9]
    ]

    while True:
        # 1 <= n <=2*10**100
        n = input().strip()

        if n  == '0':
            break

        n_len = len(n)
        tens = ord(n[n_len - 2]) - ord('0')  if n_len >= 2 else 0
        results = tens * 7
        for idx in range(1, ord(n[n_len-1])-ord('0')+1):
            results += digits[tens%2][idx]
        results %= 10
        print (results)

if __name__ == '__main__':
    main()