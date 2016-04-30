# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q591.htm
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=532
"""

def main():
    cnt = 0
    while True:
        n = int(input())
        cnt += 1
        if n == 0:
            break
        values = list(map(int, input().split()))
        avg = sum(values)//len(values)
        move = sum(val-avg for val in values if val > avg)
        print ("Set #{}".format(cnt))
        print ("The minimum number of moves is {}.".format(move))
        print ("")

if __name__ == '__main__':
    main()