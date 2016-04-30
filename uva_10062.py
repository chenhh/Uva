# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10062.htm
"""

def main():
    cnt = 0
    while True:
        try:
            data = input()
            if cnt > 0:
                print("")
            cnt += 1
            alpha_cnt = {}
            for v in data:
                if ord(v) in alpha_cnt.keys():
                    alpha_cnt[ord(v)] += 1
                else:
                    alpha_cnt[ord(v)] = 1
            output = sorted(alpha_cnt.items(), key=lambda kv:(kv[1],-kv[0]))
            for k, v in output:
                print (k, v)

        except (EOFError):
            break

if __name__ == '__main__':
    main()