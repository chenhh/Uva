# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/115/11559.pdf
"""


def main():
    while 1:
        try:
            n_person, budget, n_hotel, n_week = list(map(int, input().split()))

            min_cost = budget + 1
            for _ in range(n_hotel):
                price = int(input())
                empty_beds = list(map(int, input().split()))
                for bed in empty_beds:
                    if bed >= n_person and n_person * price <= budget:
                        cost = n_person * price
                        if cost < min_cost:
                            min_cost = cost
            if min_cost == budget + 1:
                print ("stay home")
            else:
                print (min_cost)

        except (EOFError):
            break




if __name__ == '__main__':
    main()