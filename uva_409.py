# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 2
https://uva.onlinejudge.org/external/4/409.pdf
http://luckycat.kshs.kh.edu.tw/homework/q409.htm
"""

def excuse_score(excuse, words):
    """
    excuse: string
    words: set of keywords
    """
    excuse = excuse.lower()
    len_excuse = len(excuse)

    sdx, edx = 0, 0
    excuse_words = set()
    for jdx in range(len_excuse):
        if jdx == 0 and excuse[0].isalpha():
            sdx = 0
        elif not excuse[jdx-1].isalpha() and excuse[jdx].isalpha():
            sdx = jdx

        if excuse[jdx-1].isalpha() and not excuse[jdx].isalpha():
            edx = jdx
            excuse_word = excuse[sdx:edx]
            if excuse_word in words:
                excuse_words.add(excuse_word)

    if edx != len_excuse - 1 and excuse[len_excuse-1].isalpha():
        excuse_word = excuse[sdx:len_excuse]
        if excuse_word in words:
            excuse_words.add(excuse_word)
    return len(excuse_words)


def main():
    case = 0
    while 1:
        try:
            K, E = list(map(int, input().split()))
            words = set()

            for kdx in range(K):
                word = input().lower()
                words.add(word)

            scores, excuses = [0] * E, []
            for edx in range(E):
                excuse = input()
                excuses.append(excuse)
                scores[edx] = excuse_score(excuse, words)

            case += 1
            print ("Excuse Set #{}".format(case))
            max_score = max(scores)
            for edx in range(E):
                if scores[edx] == max_score:
                    print (excuses[edx])

            print ("")
        except (EOFError):
            break

if __name__ == '__main__':
    main()