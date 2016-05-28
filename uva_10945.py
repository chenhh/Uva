# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/109/10945.pdf
"""


def main():
    while 1:
        data = input().strip()
        if data == "DONE":
            break

        word = "".join(filter(lambda x: x.isalpha(), data)).lower()
        if all(word[idx] == word[len(word) - idx - 1]
               for idx in range(len(word) // 2)):
            print("You won't be eaten!")
        else:
            print("Uh oh..")


if __name__ == '__main__':
    main()
