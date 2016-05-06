# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/117/11713.pdf
"""

def main():
    vowels = ['a', 'e', 'i', 'o', 'u']

    n = int(input())
    for _ in range(n):
        real = input()
        abstract = input()

        if len(real) != len(abstract):
            print ("No")
        elif real == abstract:
            print ("Yes")
        else:
            mutant = True
            for r, a in zip(real, abstract):
                if r not in vowels and r != a:
                    mutant = False
                elif r in vowels and a not in vowels:
                    mutant = False

                if not mutant:
                    break
            if mutant:
                print ("Yes")
            else:
                print ("No")

if __name__ == '__main__':
    main()


