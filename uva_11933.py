# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11933.pdf
http://rubyacm.blogspot.tw/2011/06/11933-splitting-numbers.html

437 (110110101)
145 292
(010010001)
(100100100)
"""

def main():
    while 1:
        v = int(input())
        if v == 0:
            break

        b, count =0,  0
        for idx in range(32):
            shift = 1 << idx
            if shift > v:
                break
            if shift & v:
                count += 1
                if count % 2 == 0:
                    b += shift

        print (v-b, b)

if __name__ == '__main__':
    main()