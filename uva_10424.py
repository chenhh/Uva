# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/104/10424.pdf
"""


def main():
    lower = str.lower
    while 1:
        try:
            name1 = filter(lambda x: x.isalpha(), input().strip())
            name2 = filter(lambda x: x.isalpha(), input().strip())
            name1 = list(map(lower, name1))
            name2 = list(map(lower, name2))
            if len(name1) == 0 and len(name2) == 0:
                print("")
                continue

            scores = [0] * 2
            for idx, name in enumerate((name1, name2)):
                values = [ord(v) - ord('a') + 1 for v in name]
                score = sum(values)
                while score // 10:
                    values = [int(v) for v in str(score)]
                    score = sum(values)
                scores[idx] = score
            # there is a space between the value and the percent symbol
            print("{:.2f} %".format(min(scores) / max(scores) * 100))
        except (EOFError):
            break


if __name__ == '__main__':
    main()
