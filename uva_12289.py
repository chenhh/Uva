# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3710
http://luckycat.kshs.kh.edu.tw/homework/q12289.htm
"""


def main():
    v = input()
    n = int(v)
    for _ in range(n):
        word = input()
        if len(word) == 5:
            num = 3
        else:
            # length 3
            err_1, err_2 = 0, 0
            one, two = 'one', 'two'
            for idx in range(3):
                if word[idx] != one[idx]:
                    err_1 += 1
                if word[idx] != two[idx]:
                    err_2 += 1
            if err_1 <= 1:
                num = 1
            elif err_2 <= 1:
                num = 2
        print (num)
            
if __name__ == '__main__':
    main()