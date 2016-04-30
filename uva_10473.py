# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10473.htm
"""

def main():
    while True:
        val = input()
        # negative
        if val[0] == '-':
            break
        # hex
        elif len(val) > 2 and val[:2] == '0x':
            print (int(val, 16))
        # decimal
        else:
            print ("0x{:X}".format(int(val)))

if __name__ == '__main__':
    main()