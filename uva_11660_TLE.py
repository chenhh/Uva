# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: TLE
difficulty: 1
https://uva.onlinejudge.org/external/116/11660.pdf

x1 = 1
x2 = 11 (one 1)
x3 = 21 (two 1s)
x4 = 1211 (one 2, two 1s)
x5 = 111221 (one 1, one 2, two 1s)
x6 = 312211 (three 1s, two 2s, one 1)
x7 = 13112221 (one 3, one 1, two 2s, two 1s)
"""
# from io import StringIO

def main():
    xs = ['']*1010
    x_next = []
    next_clear = x_next.clear
    next_append = x_next.append

    while 1:
        x, i, j =  input().split()
        if x == '0' and i == '0' and j == '0':
            break
        i, j = int(i), int(j)
        xs[0] = "".join((x, '-'))

        for idx in range(1, i):
            cnt = 1
            next_clear()
            prev_len = len(xs[idx-1])-1
            for jdx in range(min(prev_len, 1001)):
                if xs[idx-1][jdx] == xs[idx-1][jdx+1]:
                    cnt += 1
                else:
                    next_append(str(cnt))
                    next_append(xs[idx-1][jdx])
                    cnt = 1
            next_append('-')
            xs[idx] = "".join(x_next)


        print(xs[i-1][j-1])

if __name__ == '__main__':
    main()