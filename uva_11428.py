# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q11428.htm

59**3 - 58**3 = 10267
58**3 - 57**3 = 9919
"""

def main():
    # build table
    cubes = [v**3 for v in range(1, 60)]
    cube_diffs = {}
    for v1 in range(1, 60):
        for v2 in range(1, v1):
            diff = cubes[v1-1] - cubes[v2-1]
            if diff in cube_diffs.keys():
                # diff exists
                if cube_diffs[diff][1] > v2:
                    # record value with smaller v2
                    cube_diffs[diff] = (v1, v2)
            else:
                cube_diffs[diff] = (v1, v2)
 
    while True:
        N = int(input())
        if N == 0:
            break
        if N in cube_diffs.keys():
            print (cube_diffs[N][0], cube_diffs[N][1])
        else:
            print ("No solution")
            
if __name__ == '__main__':
    main()