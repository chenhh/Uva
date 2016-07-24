# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
"""

from array import array
from time import time

ARR1 = 2000
ARR_SIZE = ARR1 * ARR1


def main():
    arr1 = array('i', [0] * ARR_SIZE)
    list1 = [0] * ARR_SIZE
    list2 = [[0] * ARR1 for _ in range(ARR1)]

    t1 = time()
    for idx in range(ARR_SIZE):
        arr1[idx]
    print(time() - t1)

    t1 = time()
    for idx in range(ARR_SIZE):
        list1[idx]
    print(time() - t1)

    t1 = time()
    for idx in range(ARR1):
        for jdx in range(ARR1):
            list2[idx][jdx]
    print(time() - t1)


if __name__ == '__main__':
    main()
