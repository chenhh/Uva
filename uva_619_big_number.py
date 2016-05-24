# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/6/619.pdf
http://luckycat.kshs.kh.edu.tw/homework/q619.htm
"""

import sys

def main():
    data = sys.stdin.readlines()

    for line in data:
        num = line.strip()
        if num == '*':
            break
        
        if  num[0].isalpha():
            # word to value
            digits = list(num)
            value = ord(digits[0]) - ord('a') + 1
            for d in digits[1:]:
                value = 26 * value +  (ord(d) - ord('a') + 1)
            print ("{:<22}{:<,}".format(num, value))

        elif num[0].isnumeric():
            # value to word
            value = int(num)
            digits = []
            while value > 0:
                a, b = divmod(value, 26)
                if not b:
                    digits.append('z')
                    value = a -1
                    if a== 1:
                        break
                else:
                    digits.append(chr(b+ord('a')-1))
                    value = a
            print("{:<22}{:<,}".format("".join(reversed(digits)), int(num)))



if __name__ == '__main__':
    main()