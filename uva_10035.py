# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

http://luckycat.kshs.kh.edu.tw/homework/q10035.htm
"""

def main():
    while True:
        strs = input()
        v1, v2 = strs.split()
        if v1 == '0' and v2 == '0':
            break

        if len(v1) < len(v2):
            v1, v2 = v2, v1
        op_len = len(v2)
        v1, v2 = v1[::-1], v2[::-1]

        cnt, carry = 0, 0
        for idx in range(op_len):
            if int(v1[idx]) + int(v2[idx]) + carry > 9:
                cnt += 1
                carry = 1
            else:
                carry = 0

        if len(v1) > op_len:
            for jdx in range(op_len, len(v1)):
                if int(v1[jdx]) + carry > 9:
                    cnt += 1
                    carry = 1
                else:
                    break

        if cnt == 0:
            print ("No carry operation.")
        elif cnt == 1:
            print ('1 carry operation.')
        else:
            print ('{} carry operations.'.format(cnt))

if __name__ == '__main__':
    main()