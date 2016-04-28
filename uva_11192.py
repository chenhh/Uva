# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=23&page=show_problem&problem=2133
http://luckycat.kshs.kh.edu.tw/homework/q11192.htm
"""

def main():

    while True:
        data = input()
        if data == "0":
            break
        v, strs = data.split()
        n_grp = int(v)
        grp_len = len(strs) // n_grp
        print ("".join([strs[idx*grp_len:(idx+1)*grp_len][::-1] for idx in range(n_grp)]))

if __name__ == '__main__':
    main()
