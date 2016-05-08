# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11965.pdf
"""

def main():
    T = int(input())

    for tdx in range(T):
        N = int(input())

        print ("Case {}:".format(tdx+1))

        for ndx in range(N):
            data = list(input())
            msg = []
            spaces = 0
            for idx, c in enumerate(data):
                if c == ' ':
                    spaces += 1
                else:
                    spaces = 0
                if spaces <= 1:
                    msg.append(c)
            print ("".join(msg))

        if tdx != T-1:
            print ("")
if __name__ == '__main__':
    main()