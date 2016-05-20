# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/4/465.pdf
long int: -2,147,483,647 to 2,147,483,647 (2**31-1)
unsigned long int: 0 to 4,294,967,295 (2**32-1)
"""

def main():
    UPPER = 2**31-1
    while 1:
        try:
            expr = input()
            parses = expr.split()
            first_overflow = False
            second_overflow = False
            result_overflow = False
            if int(parses[0]) > UPPER:
                first_overflow = True
            if int(parses[2]) > UPPER:
                second_overflow = True
            if parses[1] == '+' and int(parses[0]) + int(parses[2]) > UPPER:
                result_overflow= True
            elif parses[1] == '*' and int(parses[0]) * int(parses[2]) > UPPER:
                    result_overflow = True

            if not any((first_overflow, second_overflow, result_overflow)):
                print (expr)
            else:
                print (expr)
                if first_overflow:
                    print ("first number too big")
                if second_overflow:
                    print("second number too big")
                if result_overflow:
                    print ("result too big")

        except (EOFError):
            break

if __name__ == '__main__':
    main()
