# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/101/10114.pdf

calculating the first time, measured in months, that a car buyer owes
less money than a car is worth.
"""


def main():
    while 1:
        values = input().split()
        month = int(values[0])
        down_payment = float(values[1])
        loan_amount = float(values[2])
        n_deprecation = int(values[3])
        if month < 0:
            break

        deprecation = [0] * (month + 1)
        for _ in range(n_deprecation):
            # Month 0 is the depreciation that applies immediately after
            # driving the car off the lot and is always present in the data.
            # All the other percentages are the amount of depreciation at the
            # end of the corresponding month
            # If a month is not listed, then the previous depreciation
            # percentage applies.
            # car’s initial value will be the loan amount plus the down payment.
            mon, percent = input().split()
            deprecation[int(mon)] = float(percent)

        for idx in range(1, month + 1):
            if not deprecation[idx]:
                deprecation[idx] = deprecation[idx - 1]

        initial_value = loan_amount + down_payment
        if deprecation[0]:
            pv = initial_value * (1 - deprecation[0])
        if loan_amount < pv:
            print("0 months")
        else:
            each_payment = loan_amount / month
            ans = 0
            for cnt in range(1, month + 1):
                pv = pv * (1 - deprecation[cnt])
                owed = loan_amount - each_payment * cnt
                # print (cnt, pv, owed)
                if owed < pv:
                    ans = cnt
                    break
            print(ans, "month" if ans == 1 else "months")


if __name__ == '__main__':
    main()
