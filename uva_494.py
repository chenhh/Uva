# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=6&page=show_problem&problem=435
http://luckycat.kshs.kh.edu.tw/homework/q494.htm
"""

def main():

    while True:
        try:
            words = input()
            cnt = 0
            for idx, alpha in enumerate(words):
                if idx == 0 and alpha.isalpha():
                    cnt += 1
                elif not words[idx-1].isalpha() and alpha.isalpha():
                    cnt += 1
            print (cnt)


        except (EOFError):
            break
if __name__ == '__main__':
    main()