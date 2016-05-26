# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/1/101.pdf
http://luckycat.kshs.kh.edu.tw/homework/q101.htm
"""


def simulation(act1, src, act2, tgt, piles, blocks):
    """
    piles: list of list
    blocks, record the block in which pile
    """
    if src == tgt or blocks[src] == blocks[tgt]:
        # src == tgt or src and tgt in the same pile
        return piles, blocks

    if act1 == 'move':
        # pre-action, move the blocks above a to their original piles
        for num in reversed(piles[blocks[src]]):
            if num == src:
                break
            piles[num].append(piles[blocks[src]].pop())
            blocks[num] = num

    if act2 == 'onto':
        # pre-action, move the blocks above b to their original piles
        for num in reversed(piles[blocks[tgt]]):
            if num == tgt:
                break
            piles[num].append(piles[blocks[tgt]].pop())
            blocks[num] = num

    if act1 == 'move':
        # real action, put a on b, for both act2 in 'into' and 'over'
        piles[blocks[tgt]].append(piles[blocks[src]].pop())
        blocks[src] = blocks[tgt]

    if act1 == 'pile':
        # real action, move the blocks above a to b
        src_loc = piles[blocks[src]].index(src)
        orig_src = blocks[src]
        for num in piles[blocks[src]][src_loc:]:
            piles[blocks[tgt]].append(num)
            blocks[num] = tgt

        for _ in range(len(piles[orig_src]) - src_loc):
            piles[orig_src].pop()

    return piles, blocks


def main():
    while 1:
        try:
            n_block = int(input())
            piles = [[v] for v in range(n_block)]
            # record block in which one pile
            blocks = [v for v in range(n_block)]
            while 1:
                cmd = input().split()
                if cmd[0] == 'quit':
                    for idx, block in enumerate(piles):
                        if len(block):
                            print("{}: {}".format(
                                idx, " ".join(str(v) for v in block)))
                        else:
                            print("{}:".format(idx))

                    break
                act1, src, act2, tgt = cmd
                piles, blocks = simulation(act1, int(src), act2, int(tgt),
                                           piles, blocks)
                # print (cmd)
                # print (piles)
                # print (blocks)

        except (EOFError):
            break


if __name__ == '__main__':
    main()
