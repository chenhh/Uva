# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/413.pdf
http://rubyacm.blogspot.tw/2011/09/413-up-and-down-sequences.html
"""


def main():
    while 1:
        values = list(map(int, input().split()))
        if values[0] == 0:
            break
        # pop the last zero
        values.pop()

        states = [0] * (len(values) - 1)
        # forward loop
        for idx, val in enumerate(values[1:]):
            if val > values[idx]:
                # current up
                states[idx] = 1
            elif val < values[idx]:
                # current down
                states[idx] = -1
            else:
                # tie
                if idx > 0 and states[idx - 1] != 0:
                    # current tie, but previous state is determined
                    states[idx] = states[idx - 1]

        # backward loop, some tie states are not determined in forward loop
        for idx in reversed(range(len(states) - 1)):
            if states[idx + 1] != 0 and states[idx] == 0:
                states[idx] = states[idx + 1]

        up, down = 0, 0
        ups, downs = [], []
        for state in states:
            if state == 1:
                if up == 0 and down > 0:
                    # end of down
                    downs.append(down)
                    down = 0
                up += 1
            elif state == -1:
                if up > 0 and down == 0:
                    # end of up
                    ups.append(up)
                    up = 0
                down += 1
        if up > 0:
            ups.append(up)
        if down > 0:
            downs.append(down)

        # print (states, ups, downs)
        avg_up_len = sum(ups) / len(ups) if len(ups) else 0
        avg_down_len = sum(downs) / len(downs) if len(downs) else 0

        print("Nr values = {}:  {:.6f} {:.6f}".format(len(values),
                                                      avg_up_len, avg_down_len))


if __name__ == '__main__':
    main()
