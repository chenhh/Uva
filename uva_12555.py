# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/125/12555.pdf
"""


def main():
    n_case = int(input())
    for tdx in range(1, n_case + 1):
        # using split() can't parse '6斤6兩' case
        data = input().strip()
        weight, tmp = [], []
        for idx, val in enumerate(data[:-1]):
            if '0' <= val <= '9':
                tmp.append(val)
            if '0' <= val <= '9' and not '0' <= data[idx + 1] <= '9':
                val = int("".join(tmp))
                tmp.clear()
                weight.append(val)

        if len(weight) == 2:
            # a斤 b兩
            kg = int(weight[0]) * 0.5 + int(weight[1]) * 0.05
        elif len(weight) == 1:
            kg = int(weight[0]) * 0.5
        print("Case {}: {:g}".format(tdx, kg))


if __name__ == '__main__':
    main()
