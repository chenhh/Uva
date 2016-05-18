# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/118/11830.pdf

1<=d<=9, 1<=n <10^100
"""

def main():
    while 1:
        d, n = input().split()
        if d=='0' and n == '0':
            break

        if d not in n:
            # d does not exist in n
            print (n)
        else:
            output = n.replace(d, '')
            # check all zeros
            if len(output) == 0 or all(map(lambda x:x=='0', output)):
                print (0)
            else:
                print (output)

if __name__ == '__main__':
    main()