# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status:AC
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=18&page=show_problem&problem=1637
http://luckycat.kshs.kh.edu.tw/homework/q10696.htm

n >= 101, f91(n) = n-10
n <= 100 f91(n) = f91(f91(n+11))

f91(90) = f91(f91(101))
= f91(91) = f91(f91(102))
= f91(92) = f91(f91(103))
= f91(93) = f91(f91(104))
= ......
= f91(99) = f91(f91(105))
= f91(100) = f91(f91(111))
= f91(101) = 91

 f91(N) = f91(f91(N+11))
= ... = f91(f91(f91(...f91(a)))) // 90 <= a <= 100
= f91(f91(f91(...f91(91))))
= 91
"""
def main():
    while True:
        val = input()
        n = int(val)
        if n == 0:
            break

        sol = 91 if n<=100 else  n-10
        print ("f91({}) = {}".format(n, sol))

if __name__ == '__main__':
    main()
