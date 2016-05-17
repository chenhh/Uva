# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: TLE
difficulty: 2

https://uva.onlinejudge.org/external/119/11988.pdf
http://luckycat.kshs.kh.edu.tw/homework/q11988.htm
"""

from array import array

def string_list(data):
    """
    using array to implement one direction link list
    the head, curr, tail points to the index in the link list

    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
    T  h  i  s  _  i  s  _  a  _  [  B  e  i  j  u  ]  _  t  e  x  t
    1  2  3  4  5  6  7  8  9 17 -1 12 13 14 15  0 -1 18 19 20 21 -1
    head = 11, tail = 21

    0  1  2
    a  [  b
    -1 -1  0  head: 2, tail: 0
    still TLE
    """
    n_char = len(data)
    nexts = array('l', [-1]*n_char)
    len_list = 0
    pre_head, head, tail, curr = None, None, None, None

    for idx, c in enumerate(data):
        if c == '[':
            # move to pre-head
            curr = pre_head
        elif c == ']':
            # move to tail
            curr = tail
        else:
            if len_list > 0:
                # some elements in the list
                if curr is not None:
                    # insert after current position
                    nexts[idx] = nexts[curr]
                    nexts[curr] = idx
                    if curr == tail:
                        tail = idx
                    curr = idx
                else:
                    # insert before head
                    nexts[idx] = head
                    head = curr = idx
            else:
                # first element in the list
                head = tail =curr = idx
            # update list size
            len_list += 1

    # print (nexts)
    curr = head
    outputs = []
    for _ in range(len_list):
        outputs.append(data[curr])
        curr = nexts[curr]
        if curr == -1:
            break
    return ("".join(outputs))


def list(data):
    """
    python list insert operation average time complexity is O(n), and
    it will cause TLE.
    https://wiki.python.org/moin/TimeComplexity
    """
    output = []
    curr = 0
    count = 0
    for c in data:
        if c == '[':
            curr = 0
        elif c == ']':
            curr = count
        else:
            output.insert(curr, c)
            curr += 1
            count += 1
    return ("".join(output))


def main():
    while 1:
        try:
            data = input()
            print (string_list(data))
            # print (list(data))
        except (EOFError):
            break

if __name__ == '__main__':
    main()
