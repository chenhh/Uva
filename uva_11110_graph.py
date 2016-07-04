# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/111/11110.pdf

1) A region may not necessarily contain n pairs of coordinates
   (it can be 0 as well  :roll: ).
2) If a region size is less than n, consider the output as wrong.
3) If a region is discovered more than once, consider the output as wrong.
4) The total number of *distinct* regions should be equal to n.
5) I assumed that all values are in the range [1..n].
"""

import sys


def main():
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))

    recs = iter(sys.stdin.readlines())

    while True:
        n_size = int(next(recs))
        if not n_size:
            break

        if n_size == 1:
            # always good when size == 1
            print("good")
            continue

        is_equal = True
        used_regions = set()
        images = set((idx, jdx) for idx in range(n_size)
                     for jdx in range(n_size))

        for idx in range(n_size - 1):
            data = list(map(lambda x: int(x) - 1, next(recs).split()))
            if len(data) < (n_size + n_size):
                is_equal = False

            # If a region is discovered more than once, consider
            # the output as wrong
            regions = set((data[jdx], data[jdx + 1])
                          for jdx in range(0, len(data), 2))
            if used_regions.intersection(regions):
                is_equal = False

            used_regions = used_regions.union(regions)
            images = images.difference(regions)

            if is_equal:
                # traversal
                stack = [regions.pop(), ]
                area = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for dx, dy in directions:
                        x1, y1 = x + dx, y + dy
                        if (0 <= x1 < n_size and 0 <= y1 < n_size and
                                    (x1, y1) in regions):
                            stack.append((x1, y1))
                            regions.remove((x1, y1))
                if area != n_size:
                    is_equal = False

        regions = images
        if not regions:
            is_equal = False
        else:
            stack = [regions.pop(), ]
            area = 0
            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy in directions:
                    x1, y1 = x + dx, y + dy
                    if (0 <= x1 < n_size and 0 <= y1 < n_size and
                                (x1, y1) in regions):
                        stack.append((x1, y1))
                        regions.remove((x1, y1))
            if area != n_size:
                is_equal = False

        # all elements in the list are equal or not
        print("good" if is_equal else "wrong")


if __name__ == '__main__':
    main()
