# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/101/10194.pdf

A team earns 3 points for each win,
1 point for each tie and 0 point for each loss.

Teams are ranked according to these rules (in this order):
1. Most points earned.
2. Most wins.
3. Most goal difference (i.e. goals scored - goals against)
4. Most goals scored.
5. Less games played.
6. Lexicographic order
"""

import sys
from functools import cmp_to_key


def cmp_func(t1, t2):
    """
     return a negative value for less-than, return zero if they are equal, or
     return a positive value for greater-than.
    """
    if t1['point'] != t2['point']:
        return t1['point'] - t2['point']

    if t1['n_win'] != t2['n_win']:
        return t1['n_win'] - t2['n_win']

    diff1 = t1['goal_scored'] - t1['goal_against']
    diff2 = t2['goal_scored'] - t2['goal_against']
    if diff1 != diff2:
        return diff1 - diff2

    if t1['goal_scored'] != t2['goal_scored']:
        return t1['goal_scored'] - t2['goal_scored']

    t1_game = t1['n_win'] + t1['n_lose'] + t1['n_tie']
    t2_game = t2['n_win'] + t2['n_lose'] + t2['n_tie']
    if t1_game != t2_game:
        return -(t1_game - t2_game)

    # lexical order
    name1, name2 = t1['name'].lower(), t2['name'].lower()
    if name1 < name2:
        return 1
    elif name1 > name2:
        return -1
    else:
        return 0


def main():
    recs = iter(sys.stdin.readlines())
    n_tournament = int(next(recs))

    for tdx in range(n_tournament):
        name = next(recs).strip()
        n_team = int(next(recs))
        # (name: point, win, goal_diff, score, against, n_game)
        teams = {}
        for _ in range(n_team):
            k = next(recs).strip()
            teams[k] = {'name': k, "point": 0, "goal_scored": 0,
                        "n_win": 0, 'n_lose': 0, 'n_tie': 0, "goal_against": 0}
        n_game = int(next(recs))
        # You may assume that there will not be inexistent team names.
        # and that no team will play against itself.

        # team_name_1#goals1@goals2#team_name_2
        for _ in range(n_game):
            game = next(recs).strip()
            p1 = game.find('#')
            p2 = game.find('@', p1)
            p3 = game.find('#', p2)
            team1, goal1 = game[:p1], int(game[p1 + 1:p2])
            team2, goal2 = game[p3 + 1:], int(game[p2 + 1:p3])

            if goal1 > goal2:
                teams[team1]['point'] += 3
                teams[team1]['n_win'] += 1
                teams[team2]['n_lose'] += 1
            elif goal1 < goal2:
                teams[team2]['point'] += 3
                teams[team2]['n_win'] += 1
                teams[team1]['n_lose'] += 1
            else:
                teams[team1]['point'] += 1
                teams[team2]['point'] += 1
                teams[team1]['n_tie'] += 1
                teams[team2]['n_tie'] += 1

            teams[team1]['goal_scored'] += goal1
            teams[team2]['goal_scored'] += goal2
            teams[team1]['goal_against'] += goal2
            teams[team2]['goal_against'] += goal1

        boards = sorted(teams.values(), key=cmp_to_key(cmp_func), reverse=True)

        if tdx:
            print()

        print(name)
        for bdx, board in enumerate(boards):
            print("{}) {} {}p, {}g ({}-{}-{}), {}gd ({}-{})".format(
                bdx + 1,
                board['name'],
                board['point'],
                board['n_win'] + board['n_tie'] + board['n_lose'],
                board['n_win'],
                board['n_tie'],
                board['n_lose'],
                board['goal_scored'] - board['goal_against'],
                board['goal_scored'],
                board['goal_against']
            ))


if __name__ == '__main__':
    main()
