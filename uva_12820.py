# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: 
difficulty: 1
https://uva.onlinejudge.org/external/128/12820.pdf
"""

def main():
    n_case = 0
    char_count = {}
    get = char_count.get
    while 1:
        try:
            n = int(input())
            n_case += 1
            n_cool_word = 0
           
            for idx in range(n):
                char_count.clear()
                word = input().strip()
                for c in word:
                    char_count[c] = get(c, 0) + 1
            
                n_char = len( char_count.keys())
                n_cnt = len(set(char_count.values()))
                if n_char >= 2 and n_char == n_cnt:
                    n_cool_word += 1
            
            print ("Case {}: {}".format(n_case, n_cool_word))
        except (EOFError):
            break
    

if __name__ == '__main__':
    main()

