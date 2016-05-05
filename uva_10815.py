# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/108/10815.pdf
"""
import bisect

def main():
    words = []
    while True:
        try:
            data = input().lower()

            sdx, edx = 0, 0
            data_len = len(data)
            for idx, c in enumerate(data):
                if idx !=0 and not data[idx-1].isalpha() and c.isalpha():
                    sdx = idx
                if idx !=0 and data[idx-1].isalpha() and not c.isalpha():
                    edx = idx
                    bisect.insort_left(words, data[sdx:edx].strip())

            if edx != data_len-1 and c.isalpha():
                edx = data_len
                bisect.insort_left(words, data[sdx:edx].strip())

        except (EOFError):
            for jdx, word in enumerate(words):
                if jdx == 0 and len(word) > 0:
                        print (word)
                elif words[jdx-1] != word and len(word) > 0:
                    print (word)
            break

if __name__ == '__main__':
    main()