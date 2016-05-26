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
        return blocks

    elif act1 == 'move' and act2 == 'onto':
        # puts block a onto block b after returning any blocks that are
        # staked on top of blocks a and b to their initial positions.
        pass
    elif act1 == 'move' and act2 == 'over':
        # puts block a onto the top of the stack containing block b, after
        # returning any blocks that are staked on top of block a to their
        # initial positions.
        pass
    elif act2 == 'pile' and act2 == 'onto':
        # moves the pile of blocks consisting of block a, and any blocks
        # that are stacked above block a, onto block b. All blocks on top of
        # block b are moved to their initial positions prior to the pile
        # taking place. The blocks stacked above block a retain their order
        # when moved.
        pass
    elif act2 == 'pile' and act2 == 'over':
        # puts the pile of blocks  consisting of block a, and any blocks
        # that are staked above block a, onto the top of the stack containing
        # block b
        # update record
        for block in piles[src]:
            blocks[block] = tgt
        # realization
        piles[tgt].extend(piles[src])
        piles[src].clear()


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
                        print("{}: {}".format(
                            idx, " ".join(str(v) for v in block)))
                    break
                act1, src, act2, tgt = cmd
                blocks = simulation(act1, src, act2, tgt, piles, blocks)

        except (EOFError):
            break


if __name__ == '__main__':
    main()
