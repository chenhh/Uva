# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=948

If given no. of Nodes are N Then
    Different No. of BST=Catalan(N)
    Different No. of Structurally Different Binary trees are = Catalan(N)
    Different No. of Binary Trees are=N!*Catalan(N)
"""
def Catalan(n):
    #(factorial(2*n)/factorial(n+1))
    val = 1
    for v in range(n+2, 2*n+1):
        val *= v
    return val
        

def main():
    while True:
        v = input()
        value = int(v)
        if value == 0:
            break
        print (Catalan(value))

if __name__ == '__main__':
    main()
    
