# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
http://luckycat.kshs.kh.edu.tw/homework/q12019.htm
"""
import datetime

def main():
    v = input()
    for _ in range(int(v)):
        strs = input()
        dates = [int(v) for v in strs.split()]
        obj = datetime.date(2011, dates[0], dates[1])
        day = obj.isoweekday()
        # Monday is 1 and Sunday is 7
        if day == 1:
            print ("Monday")
        elif day == 2:
            print ("Tuesday")
        elif day == 3:
            print ("Wednesday")
        elif day == 4:
            print ("Thursday")
        elif day == 5:
            print ("Friday")
        elif day == 6:
            print ("Saturday")
        elif day == 7:
            print ("Sunday")
            
if __name__ == '__main__':
    main()