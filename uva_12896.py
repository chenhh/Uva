# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
https://uva.onlinejudge.org/external/128/12896.pdf
"""

keyboards = {
    (1, 1): '.',
    (1, 2): ',',
    (1, 3): '?',
    (1, 4): '"',
    (2, 1): 'a',
    (2, 2): 'b',
    (2, 3): 'c',
    (3, 1): 'd',
    (3, 2): 'e',
    (3, 3): 'f',
    (4, 1): 'g',
    (4, 2): 'h',
    (4, 3): 'i',
    (5, 1): 'j',
    (5, 2): 'k',
    (5, 3): 'l',
    (6, 1): 'm',
    (6, 2): 'n',
    (6, 3): 'o',
    (7, 1): 'p',
    (7, 2): 'q',
    (7, 3): 'r',
    (7, 4): 's',
    (8, 1): 't',
    (8, 2): 'u',
    (8, 3): 'v',
    (9, 1): 'w',
    (9, 2): 'x',
    (9, 3): 'y',
    (9, 4): 'z',
    (0, 1): ' ',
}

def main():
    T = int(input())
    for _ in range(T):
        len_msg = int(input())
        nums = list(map(int, input().split()))
        press = list(map(int, input().split()))
        decode = "".join(keyboards[(n,p)] for n, p in zip(nums, press))
        print (decode)
    
if __name__ == '__main__':
    main()