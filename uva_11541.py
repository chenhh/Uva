# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=27&page=show_problem&problem=2536
http://luckycat.kshs.kh.edu.tw/homework/q11541.htm
"""

def main():
    T = int(input())
    for idx in range(T):
        RLE = input()
        decode = []
        alpha_locs = [idx for idx, d in enumerate(RLE) if d.isalpha()]
        n_alpha = len(alpha_locs)
        for jdx, loc in enumerate(alpha_locs):
            if jdx != n_alpha - 1:
                reps = int(RLE[loc+1:alpha_locs[jdx+1]])
            else:
                reps = int(RLE[loc+1:])
            decode.append(RLE[loc] * reps)
        print ("Case {}: {}".format(idx+1, "".join(decode)))
            
if __name__ == '__main__':
    main()