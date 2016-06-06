# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/7/706.pdf
"""


def main():
    while 1:
        data = input().split()
        if data[0] == '0':
            break
        # Each digit occupies exactly s + 2 columns and 2s + 3 rows
        s = int(data[0])
        # the number may start with 0
        num = data[1]

        col_size = s + 2
        for rdx in range(2 * s + 3):
            out = []
            for cdx, digit in enumerate(num):
                if rdx == 0:
                    # first row
                    if digit in ('1', '4'):
                        out.extend(' ' for _ in range(col_size))
                    else:
                        out.extend(' ' if sdx in (0, s + 1) else '-'
                                   for sdx in range(col_size))
                elif 1 <= rdx <= s:
                    if digit in ('1', '2', '3', '7'):
                        out.extend('|' if sdx == s + 1 else ' '
                                   for sdx in range(col_size))
                    elif digit in ('5', '6'):
                        out.extend('|' if sdx == 0 else ' '
                                   for sdx in range(col_size))
                    else:
                        out.extend('|' if sdx in (0, s + 1) else ' '
                                   for sdx in range(col_size))

                elif rdx == s + 1:
                    # the middle row
                    if digit in ('0', '1', '7'):
                        out.extend(' ' for _ in range(col_size))
                    else:
                        out.extend(' ' if sdx in (0, s + 1) else '-'
                                   for sdx in range(col_size))

                elif s + 2 <= rdx <= 2 * s + 1:
                    if digit in ('1', '3', '4', '5', '7', '9'):
                        out.extend('|' if sdx == s + 1 else ' '
                                   for sdx in range(col_size))
                    elif digit in ('2',):
                        out.extend('|' if sdx == 0 else ' '
                                   for sdx in range(col_size))
                    else:
                        out.extend('|' if sdx in (0, s + 1) else ' '
                                   for sdx in range(col_size))
                elif rdx == 2 * s + 2:
                    # last row
                    if digit in ('1', '4', '7'):
                        out.extend(' ' for _ in range(col_size))
                    else:
                        out.extend(' ' if sdx in (0, s + 1) else '-'
                                   for sdx in range(col_size))
                # there is a space between two digits
                if cdx != len(num) - 1:
                    out.append(' ')
            print("".join(out))
        print()


if __name__ == '__main__':
    main()
