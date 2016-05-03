# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/3/343.pdf
"""

def main():

    while True:
        try:
            data = input()
            x_str, y_str = data.split()

            # find min base
            min_bases = [2, 2]
            for idx, digits in enumerate([x_str, y_str]):
                for v in digits:
                    if v.isdigit():
                        min_bases[idx] = max(ord(v)-ord('0')+1,
                                             min_bases[idx])
                    else:
                        a = v.upper()
                        min_bases[idx] = max(ord(a)- ord('A')+11,
                                             min_bases[idx])

            pair = None
            for b1 in range(min_bases[0], 37):
                x = int(x_str, b1)
                if pair:
                    break
                for b2 in range(min_bases[1], 37):
                    y = int(y_str, b2)
                    if x == y:
                        pair = (b1, b2)
                        break
            if not pair:
                print ("{} is not equal to {} in any base 2..36".format(
                    x_str, y_str))
            else:
                print ("{} (base {}) = {} (base {})".format(
                    x_str, pair[0], y_str, pair[1]))

        except (EOFError):
            break


if __name__ == '__main__':
    main()