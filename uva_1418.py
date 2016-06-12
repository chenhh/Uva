# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/14/1418.pdf
http://blog.csdn.net/keshuai19940722/article/details/17440081

n teams, each team plays twice (home and away) against each other team.
win: 3, draw: 1, lose: 0 points
teams are ranked by numbers from 1 to n according to the total points.

wonder team:
  - absolutely the highest number of wins.
  - absolutely the highest number of goals scored
  - absolutely the lowest number of goals conceded
  n<=3, the worst rank of wonder team is 1
"""


def main():
    while 1:
        n = int(input())
        if n == 0:
            break
        if n <= 3:
            print(1)
        elif n == 4:
            print(2)
        else:
            print(n)


if __name__ == '__main__':
    main()
