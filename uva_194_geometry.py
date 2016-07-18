# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 4

https://uva.onlinejudge.org/external/1/194.pdf
http://www.cnblogs.com/devymex/p/3277404.html

if there are at least 3 values, then it can be solved.
"""

import sys
from math import (pi, cos, acos, sin, asin, sqrt)

EPS = 1e-6


def is_all_positive(values):
    for val in values:
        if val <= 0:
            return False
    return True


def is_positive_edge(a, b, c):
    return False if a <= 0 or b <= 0 or c <= 0 else True


def is_positive_angle(alpha, beta, gamma):
    return False if alpha <= 0 or beta <= 0 or gamma <= 0 else True


def is_satisfy_angle_rule(alpha, beta, gamma):
    return False if alpha + beta + gamma - pi > EPS else True


def is_satisfy_triangle_inequality(a, b, c):
    if (a + b <= c or a + c <= b or b + c <= a):
        # triangle inequality
        return False


def is_triangle(values):
    a, alpha, b, beta, c, gamma = values
    if a <= 0 or b <= 0 or c <= 0 or alpha <= 0 or beta <= 0 or gamma <= 0:
        return False

    if alpha + beta + gamma - pi > EPS:
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        # triangle inequality
        return False

    if (a * sin(beta) - b * sin(alpha) > EPS or
                        a * sin(gamma) - c * sin(alpha) > EPS or
                        b * sin(gamma) - c * sin(beta) > EPS):
        return False

    return True


def post_check(values):
    if is_triangle(values):
        return " ".join(":.6f".format(v for v in values))
    else:
        return "Invalid input."


def is_satisfy_law_of_sine(a, b, alpha, beta):
    return False if a * sin(beta) - b * sin(alpha) > EPS else True


def law_of_cosine_to_angle(a, b, c):
    """ to get the angle of a """
    return acos((b * b + c * c - a * a) / (2 * b * c))


def law_of_cosine_to_edge(alpha, b, c):
    """ to get the edge of alpha """
    return sqrt(b * b + c * c - 2 * b * c * cos(alpha))


def main():
    recs = iter(sys.stdin.readlines())
    n_case = int(next(recs))

    for _ in range(n_case):
        # a, alpha, b, beta, c, gamma
        values = list(map(float, next(recs).split()))
        a, alpha, b, beta, c, gamma = values

        # negative values are the unknown variables
        data_type = [1] * 6
        n_known = 6
        for idx, val in enumerate(values):
            if val <= 0:
                data_type[idx] = 0
                n_known -= 1

        if n_known <= 2:
            # all the edges or all the angles are unknown.
            print("Invalid input.")
            continue

        tri_type = "".join(data_type)

        if tri_type == '111111':
            # all edges and angles are known
            print(post_check(values))

        elif tri_type == '010101':
            # AAA, no finite solutions.
            print("Invalid input.")

        elif tri_type == '101010':
            # SSS, only three edges are known, no multiple solution.
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                # recover angles
                values[1] = law_of_cosine_to_angle(a, b, c)
                values[3] = law_of_cosine_to_angle(b, a, c)
                values[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(values))

        elif tri_type == '101001':
            # SAS (a,b,gamma)
            if gamma > pi:
                # law of angle
                print("Invalid input.")
            else:
                values[4] = law_of_cosine_to_edge(gamma, a, b)
                c = values[4]
                values[1] = law_of_cosine_to_angle(a, b, c)
                values[3] = law_of_cosine_to_angle(b, a, c)

                # post check
                print(post_check(values))

        elif tri_type == '011010':
            # SAS (alpha, b, c)
            if alpha > pi:
                # law of angle
                print("Invalid input.")
            else:
                values[0] = law_of_cosine_to_edge(alpha, b, c)
                a = values[0]
                values[3] = law_of_cosine_to_angle(b, a, c)
                values[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(values))

        elif tri_type == '100110':
            # SAS (a, beta, c)
            if beta > pi:
                # law of angle
                print("Invalid input.")
            else:

                values[2] = law_of_cosine_to_edge(beta, a, c)
                b = values[2]
                values[1] = law_of_cosine_to_angle(a, b, c)
                values[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(values))

        elif tri_type == '111000':
            # SSA (a, alpha, b)
            if alpha > pi:
                # law of angle
                print("Invalid input.")
            elif alpha > pi / 2 and a < b:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif alpha < pi / 2 and a < b * sin(alpha):
                # law of sine
                print("Invalid input.")
            elif alpha < pi / 2 and a > b * sin(alpha) and a < b:
                # law of sine
                print("More than one solution.")
            else:
                values[3] = pi - asin(b * sin(alpha) / a)
                beta = values[3]
                values[5] = pi - alpha - beta
                gamma = values[5]
                values[4] = a / sin(alpha) * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '001110':
            # SSA (b, beta, c)
            if beta > pi:
                # law of angle
                print("Invalid input.")
            elif beta > pi / 2 and b < c:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif beta < pi / 2 and b < c * sin(beta):
                # law of sine
                print("Invalid input.")
            elif beta < pi / 2 and b > c * sin(beta) and b < c:
                # law of sine
                print("More than one solution.")
            else:
                values[5] = pi - asin(c * sin(beta) / b)
                gamma = values[5]
                values[1] = pi - gamma - beta
                alpha = values[1]
                values[0] = b / sin(beta) * sin(alpha)

                # post check
                print(post_check(values))

        elif tri_type == '100011':
            # SSA (a, c, gamma)
            if gamma > pi:
                # law of angle
                print("Invalid input.")
            elif gamma > pi / 2 and c < a:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif gamma < pi / 2 and c < a * sin(gamma):
                # law of sine
                print("Invalid input.")
            elif gamma < pi / 2 and c > a * sin(gamma) and c < a:
                # law of sine
                print("More than one solution.")
            else:
                values[1] = pi - asin(a * sin(gamma) / c)
                alpha = values[1]
                values[3] = pi - gamma - alpha
                beta = values[3]
                values[2] = c / sin(gamma) * sin(beta)

                # post check
                print(post_check(values))

        elif tri_type == '110010':
            # SSA (a,alpha, c)
            if alpha > pi:
                # law of angle
                print("Invalid input.")
            elif alpha > pi / 2 and a < c:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif alpha < pi / 2 and a < c * sin(alpha):
                # law of sine
                print("Invalid input.")
            elif alpha < pi / 2 and a > c * sin(alpha) and a < c:
                # law of sine
                print("More than one solution.")
            else:
                values[5] = pi - asin(c * sin(alpha) / a)
                gamma = values[5]
                values[3] = pi - alpha - gamma
                beta = values[3]
                values[2] = a / sin(alpha) * sin(beta)

                # post check
                print(post_check(values))

        elif tri_type == '101100':
            # SSA (a, b, beta)
            if beta > pi:
                # law of angle
                print("Invalid input.")
            elif beta > pi / 2 and b < a:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif beta < pi / 2 and b < a * sin(beta):
                # law of sine
                print("Invalid input.")
            elif beta < pi / 2 and b > a * sin(beta) and b < a:
                # law of sine
                print("More than one solution.")
            else:
                values[1] = pi - asin(a * sin(beta) / b)
                alpha = values[1]
                values[5] = pi - alpha - beta
                gamma = values[5]
                values[4] = b / sin(beta) * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '001011':
            # SSA (b, c, gamma)
            if gamma > pi:
                # law of angle
                print("Invalid input.")
            elif gamma > pi / 2 and c < b:
                # law of sine, the largest angle has the longest edge
                print("Invalid input.")
            elif gamma < pi / 2 and c < b * sin(gamma):
                # law of sine
                print("Invalid input.")
            elif gamma < pi / 2 and c > b * sin(gamma) and c < b:
                # law of sine
                print("More than one solution.")
            else:
                values[3] = pi - asin(b * sin(gamma) / c)
                beta = values[3]
                values[1] = pi - gamma - beta
                alpha = values[1]
                values[0] = c / sin(gamma) * sin(alpha)

                # post check
                print(post_check(values))






        elif tri_type in ('010110', '100101', '011001'):
            # ASA, (alpha, beta, c), (a ,beta, gamma), (alpha, b, gamma)
            if alpha + beta > pi or beta + gamma > pi or alpha + gamma > pi:
                print("Invalid input.")
            else:
                if gamma <= 0:
                    values[5] = pi - alpha - beta
                    ratio = c / sin(values[5])
                    values[0] = ratio * sin(alpha)
                    values[2] = ratio * sin(beta)
                elif alpha <= 0:
                    values[1] = pi - beta - gamma
                    ratio = a / sin(values[1])
                    values[2] = ratio * sin(beta)
                    values[4] = ratio * sin(gamma)
                elif beta <= 0:
                    values[3] = pi - alpha - gamma
                    ratio = b / sin(values[3])
                    values[0] = ratio * sin(alpha)
                    values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type in ('110100', '001101', '010011',
                          '110001', '011100', '000111'):
            # AAS
            # (a, alpha, beta), (b, beta, gamma), (alpha, c, gamma)
            # (a, alpha, gamma), (alpha, b, beta), (beta c, gamma)
            pass


        elif tri_type in ('111010', '101110', '101011'):
            # SSS, three edges and one angle are known, no multiple solution.
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                # recover
                if alpha > 0:
                    values[3] = law_of_cosine_to_angle(b, a, c)
                    values[5] = law_of_cosine_to_angle(c, a, b)
                elif beta > 0:
                    values[1] = law_of_cosine_to_angle(a, b, c)
                    values[5] = law_of_cosine_to_angle(c, a, b)
                elif gamma > 0:
                    values[1] = law_of_cosine_to_angle(a, b, c)
                    values[3] = law_of_cosine_to_angle(b, a, c)

                # post check
                print(post_check(values))

        elif tri_type in ('010111', '110101', '011101'):
            # ASA
            pass

        elif tri_type in ('111100', '001111', '110011'):
            # AAS
            pass
        elif tri_type in ('110110', '101101', '011011'):
            # ASA
            pass
        elif tri_type in ('011110', '100111', '111001'):
            # ASA
            pass

        elif tri_type in ('111110', '101111', '111011'):
            # SSS, three edges and two angles are known
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                if alpha < 0:
                    values[1] = law_of_cosine_to_angle(a, b, c)
                elif beta < 0:
                    values[3] = law_of_cosine_to_angle(b, a, c)
                elif gamma < 0:
                    values[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(values))

        elif tri_type in ('011111', '110111', '111101'):
            # ASA
            pass


if __name__ == '__main__':
    main()
