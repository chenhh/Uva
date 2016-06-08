# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/127/12700.pdf
"""


def main():
    n_case = int(input())

    for tdx in range(1, n_case + 1):
        n_match = int(input())
        matches = input().strip()
        counts = {'B': 0, 'W': 0, 'T': 0, 'A': 0}
        for m in matches:
            counts[m] += 1

        if counts['A'] == n_match:
            # all matches are abandoned
            print('Case {}: ABANDONED'.format(tdx))
        elif counts['B'] + counts['A'] == n_match:
            # not all abandoned and Bangladesh wins all the others matches
            print('Case {}: BANGLAWASH'.format(tdx))
        elif counts['W'] + counts['A'] == n_match:
            # not all abandoned and WWW wins all the others matches
            print("Case {}: WHITEWASH".format(tdx))
        elif counts['B'] == counts['W']:
            print('Case {}: DRAW {} {}'.format(tdx, counts['B'], counts['T']))
        elif counts['B'] > counts['W']:
            print('Case {}: BANGLADESH {} - {}'.format(tdx, counts['B'],
                                                       counts['W']))
        elif counts['B'] < counts['W']:
            print('Case {}: WWW {} - {}'.format(tdx, counts['W'], counts['B']))


if __name__ == '__main__':
    main()
