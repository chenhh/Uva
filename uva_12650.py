# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=602&page=show_problem&problem=4379
http://luckycat.kshs.kh.edu.tw/homework/q12650.htm
"""

def main():
  while True:
    try:
        str1 = input()
        str2 = input()
        n, R = [int(v) for v in str1.split()]
        cards = [int(v) for v in str2.split()]
        if n == R:
            print ("*")
        else:
            all_cards = list(range(1, n+1))
            for card in cards:
                all_cards.remove(card)
            print ("{} ".format(" ".join(str(v) for v in all_cards)))
        
    except (EOFError):
        break

if __name__ == '__main__':
    main()