# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/113/11398.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11398.htm
"""

def main():
    codes = []
    while 1:
        data = input().strip().split()
        if data[0] == '~':
            break
        elif data[-1] != '#':
            codes.extend(data)
        else:
            codes.extend(data)
            # remove # tag
            codes.pop()
            decode = []
            flag = 0
            for block in codes:
                n_element = len(block)
                if n_element == 1:
                    flag = 1
                elif n_element == 2:
                    flag = 0
                else:
                    decode.extend([flag] * (n_element-2))

            if len(decode) > 0:
                binary = "".join(str(v) for v in decode)
                print (int(binary, 2))
            else:
                print (0)

            # reset
            codes.clear()

if __name__ == '__main__':
    main()