# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/110/11094.pdf
"""

import sys


def main():
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    recs = iter(sys.stdin.readlines())

    stack = []
    stack_append = stack.append
    stack_pop = stack.pop

    while True:
        try:
            while True:
                data = next(recs).strip()
                if data:
                    n_row, n_col = list(map(int, data.split()))
                    break

            image, chars = [], set()
            for _ in range(n_row):
                row = next(recs).strip()
                image.append(list(row))
                chars = chars.union(set(row))

            # the owned continent
            x0, y0 = list(map(int, next(recs).split()))

            if len(chars) == 1:
                # the size of owned continent is equal to the map
                print(0)
                continue

            land = image[x0][y0]
            water = [v for v in chars if v != land][0]
            image[x0][y0] = water

            stack.append((x0, y0))
            while stack:
                x, y = stack_pop()
                for dx, dy in directions:
                    x1, y1 = (x + dx), (y + dy) % n_col
                    if 0 <= x1 < n_row and image[x1][y1] == land:
                        stack_append((x1, y1))
                        image[x1][y1] = water

            # the other continent
            continent_size, max_continent_size = 0, 0
            for idx in range(n_row):
                if stack:
                    break
                for jdx in range(n_col):
                    if image[idx][jdx] == land:
                        stack.append((idx, jdx))
                        image[idx][jdx] = water
                        continent_size += 1
                        break

            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    x1, y1 = (x + dx), (y + dy) % n_col
                    if 0 <= x1 < n_row and image[x1][y1] == land:
                        stack_append((x1, y1))
                        image[x1][y1] = water
                        continent_size += 1

                if not stack:
                    max_continent_size = max(max_continent_size, continent_size)
                    continent_size = 0
                    for idx in range(n_row):
                        if stack:
                            break
                        for jdx in range(n_col):
                            if image[idx][jdx] == land:
                                stack.append((idx, jdx))
                                image[idx][jdx] = water
                                continent_size += 1
                                break
            print(max_continent_size)

        except (StopIteration):
            break


if __name__ == '__main__':
    main()
