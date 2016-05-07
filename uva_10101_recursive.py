# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

’kuti’ (10000000), ’lakh’ (100000), ’hajar’ (1000), ’shata’ (100)
999999999999999
9 kuti 99 lakh 99 hajar 9 shata 99 kuti 99 lakh 99 hajar 9 shata 99

45897458973958
45 lakh 89 hajar 7 shata 45 kuti 89 lakh 73 hajar 9 shata 58
"""

def bangla(num, msg):
    if num == 0:
        return

    if num // 10000000:
        # kuti
        bangla( num // 10000000, msg)
        msg.append("kuti")
        num %= 10000000

    if num // 100000:
        # lakh
        bangla( num // 100000, msg )
        msg.append('lakh')
        num %= 100000

    if num // 1000:
        # hajar
        bangla (num // 1000, msg)
        msg.append('hajar')
        num %= 1000

    if num // 100:
        # shata
        bangla (num // 100, msg)
        msg.append('shata')
        num %= 100

    if num:
        msg.append(num)

    return msg


def main():
    case = 0

    while True:
        try:
            # 0 <= data <= 999999999999999
            data = int(input())
            case += 1

            if data:
                print ("{:4d}. {}".format(
                    case, " ".join(str(v) for v in bangla(data, []))))
            else:
                print ("{:>4d}. 0".format(case))

        except (EOFError):
            break

if __name__ == '__main__':
    main()