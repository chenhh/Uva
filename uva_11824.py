# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/118/11824.pdf
"""

def main():
    budget = 5000000
    T = int(input())

    for _ in range(T):
        data =[]
        while 1:
            cost = int(input())
            if cost == 0 :
                break
            data.append(cost)

        # descending sort
        data.sort(reverse=True)

        total_cost = 0
        expensive = False
        for idx, c in enumerate(data):
            curr = c**(idx+1) << 1
            if (total_cost + curr) > budget:
                expensive = True
                break
            else:
                total_cost += curr

        if not expensive:
            print (total_cost)
        else:
            print ("Too expensive")

if __name__ == '__main__':
    main()