# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL

status: AC
difficulty: 1
https://uva.onlinejudge.org/external/109/10916.pdf

1960: 4-bit, 1970: 8-bit, 1980: 16-bit, 1990:32-bit,
given 1960 <= year <= 2160, (2**2, 2**3, ..., 2**22)
to find n! <= 2^(2^exp-bit) -1 < (n+1)! (2 <= exp <= 22, 2**22=4194304)
lg1 + lg2 + ... + lgn <= 2**(exp)-1, max n = 254018
"""
import bisect
import math

UPPER = 254020


def main():
    math_log2 = math.log2
    years = list(range(1960, 2170, 10))
    lg2s = [math_log2(x) for x in range(1, UPPER)]

    while 1:
        y = int(input())
        if y == 0:
            break

        idx = bisect.bisect_right(years, y)
        exp = (idx + 1)
        # 2**exp == 1<<exp
        # print ("exp:", exp, 2**exp)
        bound, cum_sum = 1 << exp, 0
        ans = -1
        for idx in range(UPPER):
            if cum_sum > bound:
                ans = idx - 1
                break
            cum_sum += lg2s[idx]
        print(ans)


if __name__ == '__main__':
    main()
