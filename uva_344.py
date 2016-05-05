# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/3/344.pdf
"""

def main():
    digits = {
        1: 'i', 2: 'ii', 3:'iii', 4:'iv', 5:'v',
        6: 'vi', 7:'vii', 8:'viii', 9:'ix',
        10: 'x', 20:'xx', 30: 'xxx', 40: 'xl',
        50: 'l', 60: 'lx', 70: 'lxx', 80: 'lxxx',
        90: 'xc', 100:'c'
    }

    # [i, v, x, c]
    romans = [0] * 100
    for val in range(1, 101):
        if val in digits.keys():
            repr = digits[val]
        else:
            if val == 100:
                repr = "c"
            else:
                tens = (val // 10) * 10
                ones = val % 10
                repr  = "{}{}".format(digits[tens], digits[ones])

        i, v, x, l, c = 0, 0, 0, 0, 0
        for d in repr:
            i += 1 if d == 'i' else 0
            v += 1 if d == 'v' else 0
            x += 1 if d == 'x' else 0
            l += 1 if d == 'l' else 0
            c += 1 if d == 'c' else 0

        if val == 1:
            romans[val-1] = [i, v, x, l, c]
        else:
            romans[val-1] = [
                romans[val-2][0] + i,
                romans[val-2][1] + v,
                romans[val-2][2] + x,
                romans[val-2][3] + l,
                romans[val-2][4] + c
            ]

    while True:
        n = int(input())
        if n == 0:
            break

        print ("{}: {} i, {} v, {} x, {} l, {} c".format(
            n, romans[n-1][0], romans[n-1][1], romans[n - 1][2],
            romans[n-1][3], romans[n-1][4]))

if __name__ == '__main__':
    main()
