# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2
http://luckycat.kshs.kh.edu.tw/homework/q107.htm
prime decomposition

height: h, h/(n+1), h/(n+1)**2, ..., h/(n+1)**k=1
number: 1, n, n**2, ..., n**k = w
given h and w
to get (1+n+n**2+...+n**(k-1)) and
       h + h/(n+1)*n + h/(n+1)**2 * n**2 + ... + h/(n+1)**k * n**k
"""

def main():
    while True:
        height, worker = map(int, input().split())
        if height == 0 and worker == 0:
            break

        if height == 1 and worker == 1:
            print ("{} {}".format(0, 1))
            continue

        # decomposition
        for np1 in range(2, height+1):
            k, tmp_height, tmp_worker = 0, height, 1
            while (tmp_height % np1 == 0 and tmp_height != 1):
                tmp_height /= np1
                tmp_worker *= (np1-1)
                k += 1
            if tmp_worker == worker:
                break
        n = np1 - 1
        # print(n, k)
        # Geometric progression
        non_workers = (worker -1)//(n-1) if n != 1 else k
        sum_heights = (n+1)*height - worker*n
        print (non_workers, sum_heights)

if __name__ == '__main__':
    main()