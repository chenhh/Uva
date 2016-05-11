# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/117/11743.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11743.htm
"""

def main():
    N = int(input())

    for _ in range(N):
        card = "".join(input().split())
        even_square = "".join(str(w) for w in
            [int(v)*2 for idx, v in enumerate(card)
             if idx %2 == 0])
        digit_sum = sum(int(v) for v in even_square)
        odd_sum = sum(int(v) for idx, v in enumerate(card) if idx %2)

        if (digit_sum + odd_sum) % 10 != 0:
            print ("Invalid")
        else:
            print ("Valid")

if __name__ == '__main__':
    main()