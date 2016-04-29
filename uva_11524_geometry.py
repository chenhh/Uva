# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2519
http://luckycat.kshs.kh.edu.tw/homework/q11524.htm
length: n1=m2, n2=m3, m1=n3
a=m1+n1, b=m2+n2, c=m3+n3

Heron's formula:
area = sqrt(s*(s-a)*(s-b)*(s-c))), s=(a+b+c)/2

in-circle:
area = a*r/2 + b*r/2+c*r/2 = (a+b+c)*r/2
"""
import math
def main():
    N = int(input())
    for _ in range(N):
        r = float(input())
        m1, n1 = map(float, input().split())
        m2, n2 = map(float, input().split())
        m3, n3 = map(float, input().split())
        # all edges scale to n1
        n2 = n2 / m2 * n1
        m2 = n1
        n3 = n3 / m3 * n2
        m3 = n2
        a,b,c = m1 + n1, m2 + n2, m3 + n3
        s = (a+b+c)/2
        t_area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        # scale value
        x = r/t_area*(a+b+c)/2
        print ("{:.4f}".format(x*x*t_area))
        
if __name__ == '__main__':
    main()
