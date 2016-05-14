# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/112/11223.pdf

there is also a third symbol, which is silence.
The code between two letters is a simple silence, the code between two words
is a double silence.
Simple and double silences are represented by a single space character and
two space characters respectively.
"""

def main():
    morse = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '-----': '0',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '.-.-.-': '.',
        '--..--': ',',
        '..--..': '?',
        '.----.': '\'',
        '-.-.--': '!',
        '-..-.': '/',
        '-.--.': '(',
        '-.--.-': ')',
        '.-...': '&',
        '---...': ':',
        '-.-.-.': ';',
        '-...-': '=',
        '.-.-.': '+',
        '-....-': '-',
        '..--.-': '_',
        '.-..-.': '"',
        '.--.-.': '@'
    }

    T = int(input())
    for tdx in range(T):
        # split two spaces
        codes = input().split('  ')
        decodes = []
        for code in codes:
            # split one space
            cs = code.split()
            # join one space
            decodes.append("".join(morse[v] for v in cs))

        print ("Message #{}".format(tdx+1))
        # join two spaces
        print (" ".join(decodes))
        if tdx != T-1:
            print ("")

if __name__ == '__main__':
    main()