# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=564

"""
import math

def main():
    while True:
        try:
            v = input()
            value = int(v)
            print ("{}!".format(value))
            print ("{}".format(math.factorial(value)))
        except (EOFError):
            break

if __name__ == '__main__':
    main()
