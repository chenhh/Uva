# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/5/514.pdf
http://luckycat.kshs.kh.edu.tw/homework/q514.htm
"""


def main():
    while 1:
        N = int(input())
        if N == 0:
            break

        for _ in range(N):
            # get trains position
            out_trains = list(map(int, input().split()))
            if out_trains[0] == 0:
                break

            ans, in_train, stack = True, 1, []
            for odx, out_train in enumerate(out_trains):
                while in_train < out_train:
                    # push the input into stack until the output is satisfied
                    stack.append(in_train)
                    in_train += 1

                if in_train == out_train:
                    # if the output does not equal to the top element
                    # of the stack,  the output must not be produced by the
                    # stack.
                    in_train += 1
                else:
                    if out_train != stack[-1]:
                        ans = False
                        break
                    else:
                        stack.pop()

            print("Yes" if ans else "No")

        # show blank between two cases
        print("")

if __name__ == '__main__':
    main()
