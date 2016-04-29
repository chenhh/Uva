# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status:
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q579.htm
"""

def main():
    data = int(input())
    for _ in range(data):
        N = int(input())
        code = "".join(str(v) for v in range(1, N+1))
        cnt = [0] * 10
        for d in code:
            cnt[int(d)] += 1
        print (" ".join(str(v) for v in cnt))

if __name__ == '__main__':
    main()