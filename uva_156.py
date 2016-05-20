# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/1/156.pdf
print the words which are not re-arrangement of others in lexical order.
"""

def main():
    words = {}
    while 1:
        data = input().split()
        if data[0] != '#':
            for word in data:
                key = "".join(sorted(word.lower()))
                try:
                    words[key][0] += 1
                    words[key].append(word)
                except (KeyError):
                    words[key] = [1,]
                    words[key].append(word)
        else:
            rel_ananagram = sorted(v[1] for k, v in words.items()
                                   if v[0] == 1)
            for gram in rel_ananagram:
                print (gram)
            break

if __name__ == '__main__':
    main()