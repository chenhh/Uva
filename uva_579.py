# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q579.htm
math

"""
def main():
    while True:
        curr = input()
        if curr == "0:00":
            break
        h, m = [int(v) for v in curr.split(':')]

        h_angle = h * 30 + m * 0.5
        m_angle = m * 6
        diff_angle = abs(h_angle - m_angle)
        sol = diff_angle if diff_angle <=180 else 360 - diff_angle

        print ("{:.3f}".format(sol))

if __name__ == '__main__':
    main()