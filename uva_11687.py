# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

http://luckycat.kshs.kh.edu.tw/homework/q11687.htm
"""

def main():
    while 1:
        x = input().strip()
        if x == "END":
            break

        if x == str(len(x)):
            idx = 1
        else:
            idx = 1
            while 1:
                len_x = len(x)
                len_xx = len(str(len_x))
                idx += 1
                # print (len_x, len_xx)
                if len_x == len_xx:
                    break
                x = str(len_x)
        print (idx)

if __name__ == '__main__':
    main()