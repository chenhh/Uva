# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/106/10683.pdf
The sample output are wrong:
00000000
23595999
12000000
14273467
02475901

the AC output should be
0000000
9999998 (not 9999999)
5000000
6024846
1166552
"""

BASE_RANGE = 8640000
DEC_RANGE = 10000000


def main():
    while 1:
        try:
            curr = input().strip()
            # float precision issue
            base_cc = (int(curr[:2]) * 360000 + int(curr[2:4]) * 6000 +
                       int(curr[4:6]) * 100 + int(curr[6:]))
            # 10,000,000 / 8,640,000 = 125 / 108
            dec_base_cc = int(base_cc * 125 / 108)
            print("{:07d}".format(dec_base_cc))
        except (EOFError):
            break


if __name__ == '__main__':
    main()
