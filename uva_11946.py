# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/119/11946.pdf
"""

def main():
    codebook = {'0':'O', '1':'I', '2':'Z', '3':'E', '4':'A',
             '5':'S', '6':'G', '7':'T', '8':'B', '9':'P' }
    T = int(input())
    for tdx in range(T):
        if tdx >0 :
            print("")

        while True:
            try:
                code = list(input())
                if len(code) == 0:
                    break
            except (EOFError):
                break

            decode = []
            for c in code:
                if c in codebook.keys():
                    decode.append(codebook[c])
                else:
                    decode.append(c)
            print ("".join(decode))

if __name__ == '__main__':
    main()