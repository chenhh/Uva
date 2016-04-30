# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q10082.htm
"""

def main():
    key_dict = {'2':'1', '3':'2', '4':'3', '5':'4', '6':'5', '7':'6',
                '8':'7', '9':'8', '0':'9', '-':'0', '=':'-', 'W':'Q',
                'E':'W', 'R':'E', 'T':'R', 'Y':'T', 'U':'Y', 'I':'U',
                'O':'I', 'P':'O', '[':'P', ']':'[', '\\':']', 'S':'A',
                'D':'S', 'F':'D', 'G':'F', 'H':'G', 'J':'H', 'K':'J',
                'L':'K', ';':'L', "'":';', 'X':'Z', 'C':'X', 'V':'C',
                'B':'V', 'N':'B', 'M':'N', ',':'M', '.':',', '/':".",
                ' ': ' '}
    while True:
        try:
            data = input()
            msg = [key_dict[v] for v in data]
            print ("".join(msg))

        except (EOFError):
            break

if __name__ == '__main__':
    main()