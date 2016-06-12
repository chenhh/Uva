# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/154.pdf
"""
# roygb
colors = {'r': 0, 'o': 1, 'y': 2, 'g': 3, 'b': 4}


def main():
    block = []
    while 1:
        city = input().strip()
        if city[0] == '#':
            break
        elif city[0] != 'e':
            bins = city.split(',')
            data = [''] * 5
            for bin in bins:
                c, w = bin.split('/')
                data[colors[c]] = w
            block.append("".join(data))
        else:
            # print (block)
            scores = [[0 for _ in range(len(block))] for _ in range(len(block))]
            # print (scores)
            best, best_idx = 0, 0
            for idx in range(len(block)):
                for jdx in range(idx + 1, len(block)):
                    b1, b2 = block[idx], block[jdx]
                    score = sum(1 if b1[kdx] == b2[kdx] else 0
                                for kdx in range(5))
                    # print(idx, jdx, b1, b2, score)
                    scores[idx][jdx] = scores[jdx][idx] = score
                curr = sum(scores[idx])
                if curr >= best:
                    best = curr
                    best_idx = idx + 1
            # print (scores)
            print(best_idx)
            block.clear()


if __name__ == '__main__':
    main()
