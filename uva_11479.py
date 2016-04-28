# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
http://luckycat.kshs.kh.edu.tw/homework/q11479.htm
"""
def main():
    v = input()
    n_data = int(v)
    for cnt in range(n_data):
        strs = input()
        edges = sorted(map(lambda x:int(x), strs.split()))
        if edges[0] <= 0 or edges[1] <=0 or edges[2] <=0:
            # some edge values are negative or equal to zero
            sol = "Invalid"
        elif  edges[0] + edges[1] <= edges[2]:
            sol = "Invalid"
        elif edges[0] == edges[1] == edges[2]:
            sol = "Equilateral"
        elif edges[0] == edges[1] or edges[1] == edges[2]:
            sol = "Isosceles"
        elif edges[0] != edges[1] != edges[2]:
            sol = "Scalene"
        print ("Case {}: {}".format(cnt+1, sol))
       
if __name__ == '__main__':
    main()