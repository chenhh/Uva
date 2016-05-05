# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/6/644.pdf

no two codes within a set of codes are the same
each code has at least one bit and no more than ten bits, and that
each set has at least two codes and no more than eight.

only shorter code can be prefix of longer code.
"""

def main():
    group = 0
    codes = []
    while True:
        try:
            data = input().strip()

            if data == '9':
                group += 1
                decodable = True
                n_code = len(codes)
                codes = sorted(codes, key=len)

                for idx in range(n_code):
                    prefix_len = len(codes[idx])
                    if not decodable:
                        break
                    for jdx in range(idx+1, n_code):
                        if (len(codes[jdx]) != prefix_len and
                            codes[idx] == codes[jdx][:prefix_len]):
                            decodable = False
                            break

                print ("Set {} is ".format(group), end="")
                if decodable:
                    print ("immediately decodable")
                else:
                    print ("not immediately decodable")
                # clean
                codes = []
            else:
                codes.append(data)
        except (EOFError):
            break

if __name__ == '__main__':
    main()