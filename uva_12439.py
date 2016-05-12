# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q12439.htm
"""

def main():
    months = {"January" :1, "February": 2, "March": 3, "April": 4,
              "May": 5, "June": 6, "July": 7, "August": 8, "September": 9,
             "October": 10, "November":11, "December": 12}

    T = int(input())
    for tdx in range(T):
        d1 = input().split()
        d2 = input().split()
        # print (d1, d2)
        years =[0]*2
        for idx, (m,d,y) in enumerate((d1, d2)):
            if months[m] <=2 and int(d[:-1]) <= 28:
                years[idx] = int(y)
            else:
                years[idx] = int(y)+1

        days = []
        for year in years:
            days.append(year//4 - year//100 + year//400)

        if (years[0] %4 ==0 and years[0] % 100 != 0) or years[0] % 400 == 0:
            print (days[1] - days[0]+1)
        else:
            print (days[1]- days[0])

if __name__ == '__main__':
    main()



