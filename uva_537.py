# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/5/537.pdf
"""


def unit(msg):
    value = 0
    if msg[-1] == 'm':
        value = float(msg[:-1]) / 1000
    elif msg[-1] == 'k':
        value = float(msg[:-1]) * 1000
    elif msg[-1] == 'M':
        value = float(msg[:-1]) * 1000000
    else:
        value = float(msg)
    return value


def main():
    n_case = int(input())
    for tdx in range(n_case):
        question = input().strip()
        # Either ‘P’ and ‘U’, ‘P’ and ‘I’, or ‘U’ and ‘I’ will be given.
        p_sdx = question.find('P=')
        u_sdx = question.find('U=')
        i_sdx = question.find('I=')

        print("Problem #{}".format(tdx + 1))
        if p_sdx == -1:
            # U, I are given
            u_edx = question.find('V', u_sdx)
            i_edx = question.find('A', i_sdx)
            voltage = unit(question[u_sdx + 2:u_edx])
            current = unit(question[i_sdx + 2:i_edx])
            print("P={:.2f}W".format(voltage * current))

        elif u_sdx == -1:
            # P, I are given
            p_edx = question.find('W', p_sdx)
            i_edx = question.find('A', i_sdx)
            power = unit(question[p_sdx + 2:p_edx])
            current = unit(question[i_sdx + 2:i_edx])
            print("U={:.2f}V".format(power / current))
        elif i_sdx == -1:
            # P, U are given
            p_edx = question.find('W', p_sdx)
            u_edx = question.find('V', u_sdx)
            power = unit(question[p_sdx + 2:p_edx])
            voltage = unit(question[u_sdx + 2:u_edx])
            print("I={:.2f}A".format(power / voltage))
        print()


if __name__ == '__main__':
    main()
