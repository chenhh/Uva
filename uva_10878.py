# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10878.htm
ascii
"""

def main():
    cnt = 0
    msg = []
    while True:
        data = input()
        if data == "___________":
            cnt += 1
            if cnt %2 == 0:
                if msg[-1] == '\n':
                    msg.pop()
                print ("".join(msg))
                break
            else:
                continue
       
        # decode
        data = data[2:10]
        binary = [0]*7
        for idx in range(4):
            binary[idx] = 1 if data[idx] == 'o' else 0
        for idx in range(3):
            binary[4+idx] = 1 if data[5+idx] == 'o' else 0
        char = chr(int("".join(str(v) for v in binary), 2))
        msg.append(char)
        
if __name__ == '__main__':
    main()