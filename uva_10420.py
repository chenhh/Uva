# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/104/10420.pdf
the same name in the same country are different.
"""

def main():
    n = int(input())

    loved = {}
    for _ in range(n):
        data = input().split()
        country = data[0]
        name = " ".join(data[1:])

        if country not in loved.keys():
            loved[country] = [name, ]
        else:
            loved[country].append(name)

    for key in sorted(loved.keys()):
        print ("{} {}".format(key, len(loved[key])))

if __name__ == '__main__':
    main()