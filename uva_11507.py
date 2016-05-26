# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11507.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11507.htm

(current direction * act = next direction)
xy = y, x(-y) = -y, xz = z, x(-z) = -z
yy = -x, y(-y) = x, yz = y, y(-z) = y
zy = z, z(-y) = z, zz = -x, z(-z) = x

(-x)y = -y, (-x)(-y) = y, (-x)z = -z, (-x)(-z) = z
(-y)y = x, (-y)(-y)= -x, (-y)z = -y, (-y)(-z) = -y
(-z)y = -z, (-z)(-y) = -z, (-z)z = x, (-z)(-z) = -x
"""

states = {
    '+x+y': '+y',
    '+x-y': '-y',
    '+x+z': '+z',
    '+x-z': '-z',
    '+y+y': '-x',
    '+y-y': '+x',
    '+y+z': '+y',
    '+y-z': '+y',
    '+z+y': '+z',
    '+z-y': '+z',
    '+z+z': '-x',
    '+z-z': '+x',
    '-x+y': '-y',
    '-x-y': '+y',
    '-x+z': '-z',
    '-x-z': '+z',
    '-y+y': '+x',
    '-y-y': '-x',
    '-y+z': '-y',
    '-y-z': '-y',
    '-z+y': '-z',
    '-z-y': '-z',
    '-z+z': '+x',
    '-z-z': '-x',
}


def main():
    while 1:
        L = int(input())
        if not L:
            break

        bends = input().split()
        current = '+x'
        for bend in bends:
            if bend == 'No':
                continue
            current = states["{}{}".format(current, bend)]
        print(current)


if __name__ == '__main__':
    main()
