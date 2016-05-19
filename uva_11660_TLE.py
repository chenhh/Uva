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
from io import StringIO

def main():
    xs = ['']*1010

    while 1:
        x, i, j =  input().split()
        if x == '0' and i == '0' and j == '0':
            break
        i, j = int(i), int(j)
        xs[0] = "".join((x, '-'))

        for idx in range(1, i):
            cnt = 1
            # x_next = []
            x_next = StringIO()
            for jdx in range(len(xs[idx-1])-1):
                if jdx > 1000:
                    break
                if xs[idx-1][jdx] == xs[idx-1][jdx+1]:
                    cnt += 1
                else:
                    # x_next.append(str(cnt))
                    # x_next.append(xs[idx-1][jdx])
                    x_next.write(str(cnt))
                    x_next.write(xs[idx-1][jdx])
                    cnt = 1
            # x_next.append('-')
            x_next.write('-')
            # xs[idx] = "".join(x_next)
            xs[idx] = x_next.getvalue()

        print(xs[i-1][j-1])

if __name__ == '__main__':
    main()