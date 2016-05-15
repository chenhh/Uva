# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2
status: AC
difficulty: 1

https://uva.onlinejudge.org/external/4/489.pdf
http://luckycat.kshs.kh.edu.tw/homework/q489.htm
set
"""

def main():
    while 1:
        round = int(input())
        if round == -1:
            break

        answer = set(input().strip())
        guess = list(input().strip())

        wrong = 0
        user_win = False
        for c in guess:
            if c in answer:
                # correct guess
                answer.remove(c)
                if not len(answer):
                    # guess all char in answer
                    user_win = True
                    break
            else:
                # wrong guess
                wrong += 1
                if wrong >= 7:
                    # Hangman finish
                    break

        print ("Round {}".format(round))
        if user_win:
            print ("You win.")
        elif wrong>=7:
            print ("You lose.")
        else:
            print ("You chickened out.")

if __name__ == '__main__':
    main()





