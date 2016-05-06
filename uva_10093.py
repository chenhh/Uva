# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/100/10093.pdf
　　+265
　　　　-5464
Both the cases in uDebug gave the answers "such number is impossible!"
but in uva judge, the answers are 14 and 20, respectivey.

"""
import bisect

def to_decimal(data, base):
    """
    data may be a negative number
    """
    if 2 <= base <= 36:
        return int(data, base)
    else:
        negative = False
        rec = data

        if data[0] == '+':
            rec = data[1:]
        elif data[0] == '-':
            negative = True
            rec = data[1:]

        val = 0
        for idx, d in enumerate(rec):
            val *= base
            if '0' <= d <='9':
                diff = ord(d) - ord('0')
            elif 'A' <= d <= 'Z':
                diff = ord(d) - ord('A') + 10
            elif 'a' <= d <='z':
                diff = ord(d) - ord('a') + 36
            val += diff
        return val if not negative else -val


def main():
    bases = [str(v) for v in range(10)]
    bases.extend([chr(v) for v in range(ord('A'), ord('Z')+1)])
    bases.extend([chr(v) for v in range(ord('a'), ord('z') + 1)])

    while True:
        try:
            num = input().strip()

            # determine least base
            min_base = max(bisect.bisect_right(bases, max(c for c in num)), 2)

            solvable = False
            for b in range(min_base, 63):
                value = to_decimal(num, b)
                if value % (b - 1) == 0:
                    solvable = True
                    break

            if solvable:
                print (b)
            else:
                print ("such number is impossible!")

        except (EOFError):
            break

if __name__ == '__main__':
    main()