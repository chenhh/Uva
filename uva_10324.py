# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: 
difficulty: 1

https://uva.onlinejudge.org/external/103/10324.pdf
http://luckycat.kshs.kh.edu.tw/homework/q10324.htm

The input ends with an empty string that is a line containing only the 
new line character, this string should not be processed. 
The input may also with end of file. 
"""

def main():
    case = 0
    while 1:
        try:
            data = input()
            if not len(data):
                break
            case += 1
            print ("Case {}".format(case))
            
            value =  int(data[0])
            cum_sum = [value,]
            for idx in range(1, len(data)):
                value += int(data[idx])
                cum_sum.append(value)
            # print ('cum_sum:', cum_sum)
            n_query = int(input())
            
            for _ in range(n_query):
                lo, hi = list(map(int, input().split()))
                # end may exceed the length of data
                sdx, edx = min(lo, hi), min(max(lo,hi), len(data)-1)
                if (cum_sum[sdx] == cum_sum[edx] or 
                    cum_sum[edx] - cum_sum[sdx] == edx-sdx):
                    print ("Yes")
                else:
                    print ("No")
               
        except (EOFError):
            break

if __name__ == '__main__':
    main()
