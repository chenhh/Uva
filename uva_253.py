# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1
http://luckycat.kshs.kh.edu.tw/homework/q253.htm
http://knightzone.org/?p=1966
"""

def main():
    while True:
        try:
            colors = input()
            src = colors[:6]
            tgt = colors[6:]

            if src == tgt:
                # 123456 = 123456
                print("TRUE")
                continue
            if (src[0] == tgt[0] and src[5] == tgt[5]):
                # 135246, 142536, 154326
                if (src[1] == tgt[2] and src[2] == tgt[4] and
                            src[3] == tgt[1] and src[4] == tgt[3]):
                    # 135246 (024135)
                    print("TRUE")
                    continue
                if (src[1] == tgt[3] and src[2] == tgt[1] and
                            src[3] == tgt[4] and src[4] == tgt[2]):
                    # 142536 (031325)
                    print("TRUE")
                    continue
                if (src[1] == tgt[4] and src[2] == tgt[3] and
                            src[3] == tgt[2] and src[4] == tgt[1]):
                    # 154326 (043215)
                    print("TRUE")
                    continue

            if (src[0] == tgt[1] and src[5] == tgt[4]):
                # 214365, 231645, 246135, 263415
                if (src[1] == tgt[0] and src[2] == tgt[3] and
                            src[3] == tgt[2] and src[4] == tgt[5]):
                    # 214365 (103254)
                    print("TRUE")
                    continue
                if (src[1] == tgt[2] and src[2] == tgt[0] and
                            src[3] == tgt[5] and src[4] == tgt[3]):
                    # 231645 (120534)
                    print("TRUE")
                    continue
                if (src[1] == tgt[3] and src[2] == tgt[5] and
                            src[3] == tgt[0] and src[4] == tgt[2]):
                    # 246135 (135024)
                    print("TRUE")
                    continue
                if (src[1] == tgt[5] and src[2] == tgt[2] and
                            src[3] == tgt[3] and src[4] == tgt[0]):
                    # 263415 (152304)
                    print("TRUE")
                    continue

            if (src[0] == tgt[2] and src[5] == tgt[3]):
                # 312564, 326154, 351624, 365214
                if (src[1] == tgt[0] and src[2] == tgt[1] and
                            src[3] == tgt[4] and src[4] == tgt[5]):
                    # 312564 (201453)
                    print("TRUE")
                    continue
                if (src[1] == tgt[1] and src[2] == tgt[5] and
                            src[3] == tgt[0] and src[4] == tgt[4]):
                    # 326154 (215043)
                    print("TRUE")
                    continue
                if (src[1] == tgt[4] and src[2] == tgt[0] and
                            src[3] == tgt[5] and src[4] == tgt[1]):
                    # 351624 (240513)
                    print("TRUE")
                    continue
                if (src[1] == tgt[5] and src[2] == tgt[4] and
                            src[3] == tgt[1] and src[4] == tgt[0]):
                    # 365214 (254103)
                    print("TRUE")
                    continue

            # reverse case
            if (src[0] == tgt[3] and src[5] == tgt[2]):
                # 415263, 421653, 456123, 462513
                if (src[1] == tgt[0] and src[2] == tgt[4] and
                            src[3] == tgt[1] and src[4] == tgt[5]):
                    # 415263 (304152)
                    print("TRUE")
                    continue
                if (src[1] == tgt[1] and src[2] == tgt[0] and
                            src[3] == tgt[5] and src[4] == tgt[4]):
                    # 421653 (310542)
                    print("TRUE")
                    continue
                if (src[1] == tgt[4] and src[2] == tgt[5] and
                            src[3] == tgt[0] and src[4] == tgt[1]):
                    # 456123 (345012)
                    print("TRUE")
                    continue
                if (src[1] == tgt[5] and src[2] == tgt[1] and
                            src[3] == tgt[4] and src[4] == tgt[0]):
                    # 462513 (351402)
                    print("TRUE")
                    continue

            if (src[0] == tgt[4] and src[5] == tgt[1]):
                # 513462, 536142, 541632, 564312
                if (src[1] == tgt[0] and src[2] == tgt[2] and
                            src[3] == tgt[3] and src[4] == tgt[5]):
                    # 513462 (402351)
                    print("TRUE")
                    continue
                if (src[1] == tgt[2] and src[2] == tgt[5] and
                            src[3] == tgt[0] and src[4] == tgt[3]):
                    # 536142 (425031)
                    print("TRUE")
                    continue
                if (src[1] == tgt[3] and src[2] == tgt[0] and
                            src[3] == tgt[5] and src[4] == tgt[2]):
                    # 541632 (430521)
                    print("TRUE")
                    continue

                if (src[1] == tgt[5] and src[2] == tgt[3] and
                            src[3] == tgt[2] and src[4] == tgt[0]):
                    # 564312 (453201)
                    print("TRUE")
                    continue

            if (src[0] == tgt[5] and src[5] == tgt[0]):
                # 624351, 632541, 645231, 653421
                if (src[1] == tgt[1] and src[2] == tgt[3] and
                            src[3] == tgt[2] and src[4] == tgt[4]):
                    # 624351 (513240)
                    print("TRUE")
                    continue
                if (src[1] == tgt[2] and src[2] == tgt[1] and
                            src[3] == tgt[4] and src[4] == tgt[3]):
                    # 632541 (521430)
                    print("TRUE")
                    continue
                if (src[1] == tgt[3] and src[2] == tgt[4] and
                            src[3] == tgt[1] and src[4] == tgt[2]):
                    # 645231,(534120)
                    print("TRUE")
                    continue
                if (src[1] == tgt[4] and src[2] == tgt[2] and
                            src[3] == tgt[3] and src[4] == tgt[1]):
                    # 653421 (542310)
                    print("TRUE")
                    continue

            # print ("TRUE {}".format(pat) if ans else "FALSE {}".format(pat))
            print("FALSE")

        except (EOFError):
            break


if __name__ == '__main__':
    main()
