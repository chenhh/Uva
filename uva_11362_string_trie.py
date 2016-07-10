# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/113/11362.pdf

only a short value can be prefix of a long value
A phone number is a sequence of at most ten digits.
"""

import sys


def sequential_main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))
    for _ in range(n_case):
        n_phone = int(next(recs))
        phones = [next(recs).strip() for _ in range(n_phone)]
        trie = {}

        consistent = True
        for phone in phones:
            curr = trie
            len_phone = len(phone)
            for cdx, v in enumerate(phone):
                curr.setdefault(v, {})
                curr = curr[v]

                if '#' in curr.keys():
                    # some phones are the prefix of this phone.
                    consistent = False

                if cdx == len_phone - 1:
                    # end of a phone
                    curr['#'] = True
                    if len(curr.keys()) > 1:
                        # the phone is prefix of other phones.
                        consistent = False

            if not consistent:
                break

        # pprint (trie)
        print("YES" if consistent else "NO")


if __name__ == '__main__':
    sequential_main()
