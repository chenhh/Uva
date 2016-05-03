# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/4/445.pdf
"""

def decode(row):
    sdx = 0
    reps, symbols = [], []
    for edx in range(1, len(row)):
        if not row[edx].isdigit():
            if edx - sdx == 1:
                reps.append(int(row[sdx]))
            else:
                reps.append(sum(int(row[kdx]) for kdx in range(sdx, edx)))
            if row[edx] == 'b':
                symbols.append(' ')
            else:
                symbols.append(row[edx])
            sdx = edx + 1

    maze = "".join(reps[idx]*symbols[idx] for idx in range(len(reps)))
    return maze

def main():
    while True:
        try:
            data = input()
            if data == "":
                print ("")
            else:
                rows = data.split('!')
                for row in rows:
                    print(decode(row))

        except (EOFError):
            break

if __name__ == '__main__':
    main()