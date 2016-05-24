# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/486.pdf
http://www.aichengxu.com/view/2499293

negative nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine
-999999999 = 999*1000000 + 999*1000 + 999
"""

units = {
    'negative': -1, 'zero': 0, 'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
    'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
    'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000
}


def parse(words, sdx, edx, debug=False):
    """ recursive while the units are million, thousand, or hundred. """
    if sdx >= edx:
        return 0
    elif sdx - edx == 1:
        return units[words[sdx]]
    else:
        million_idx = 0
        thousand_idx = 0
        hundred_idx = 0
        value = 0
        for idx in range(sdx, edx):
            if words[idx] == 'million':
                million_idx = idx
            if words[idx] == 'thousand':
                thousand_idx = idx
            if words[idx] == 'hundred':
                hundred_idx = idx
            value += units[words[idx]]
        if debug:
            print(sdx, edx, million_idx, thousand_idx, hundred_idx, value)
        if million_idx:
            return (parse(words, sdx, million_idx) * 1000000 +
                    parse(words, million_idx + 1, edx))
        if thousand_idx:
            return (parse(words, sdx, thousand_idx) * 1000 +
                    parse(words, thousand_idx + 1, edx))
        if hundred_idx:
            return (parse(words, sdx, hundred_idx) * 100 +
                    parse(words, hundred_idx + 1, edx))
        return value


def main():
    while 1:
        try:
            words = input().split()
            if words[0] == 'negative':
                print('-{}'.format(parse(words, 1, len(words))))
            else:
                print(parse(words, 0, len(words)))

        except (EOFError):
            break


if __name__ == '__main__':
    main()
