# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/122/12250.pdf
"""

lang = {
    'HELLO': 'ENGLISH',
    'HOLA': 'SPANISH',
    'HALLO': 'GERMAN',
    'BONJOUR': 'FRENCH',
    'CIAO': 'ITALIAN',
    'ZDRAVSTVUJTE': 'RUSSIAN'
}


def main():
    case = 0
    while 1:
        word = input()
        if word == "#":
            break
        case += 1
        try:
            print('Case {}: {}'.format(case, lang[word]))
        except (KeyError):
            print('Case {}: UNKNOWN'.format(case))


if __name__ == '__main__':
    main()
