# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2624
http://luckycat.kshs.kh.edu.tw/homework/q11577.htm
"""

def main():
    v = input()
    n_data = int(v)
    for cnt in range(n_data):
        inputs = input()
        lowers = inputs.lower()
        alpha_cnt = [0] * 26
        for alpha in lowers:
            if 'a' <= alpha <='z':
                alpha_cnt[ord(alpha) - ord('a')] += 1
        max_value = max(alpha_cnt)
        max_alphas = [chr(idx+ord('a')) for idx, cnt in enumerate(alpha_cnt) if max_value == cnt]
        print ("".join(max_alphas))
            
if __name__ == '__main__':
    main()