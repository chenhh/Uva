# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/2/263.pdf
"""


def main():
    while 1:
        value = input().strip()
        if value == '0':
            break

        print("Original number was {}".format(value))
        len_chain = 0
        chain = {int(value)}
        current = value
        while 1:
            ascend = int("".join(sorted(current)))
            descend = int("".join(sorted(current, reverse=True)))
            diff = descend - ascend
            print("{} - {} = {}".format(descend, ascend, diff))
            len_chain += 1
            if diff in chain:
                break

            current = str(diff)
            chain.add(diff)
        print("Chain length {}\n".format(len_chain))


if __name__ == '__main__':
    main()
