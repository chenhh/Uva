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


def is_triangle(values, debug=True):
    a, alpha, b, beta, c, gamma = values
    if a <= 0 or b <= 0 or c <= 0 or alpha <= 0 or beta <= 0 or gamma <= 0:
        if debug:
            print("some negative values.")
        return False

    if alpha + beta + gamma - pi > EPS:
        if debug:
            print("the sum of angles not equal to pi.",
                  sum(alpha + beta + gamma))
        return False

    if a + b <= c or a + c <= b or b + c <= a:
        # triangle inequality
        if debug:
            print("not satisfying trinagle inequality.")
        return False

    a2 = a * a
    b2 = b * b
    c2 = c * c
    ab = a * b
    ac = a * c
    bc = b * c
    sin_alpha = sin(alpha)
    sin_beta = sin(beta)
    sin_gamma = sin(gamma)
    if (a * sin_beta - b * sin_alpha > EPS or
                        a * sin_gamma - c * sin_alpha > EPS or
                        b * sin_gamma - c * sin_beta > EPS):
        if debug:
            print("not satisfying law of sine.")
        return False

    if (a2 - b2 - b2 + 2 * bc * cos(alpha) > EPS or b2 - a2 - c2 + 2 * ac * cos(
            beta) > EPS or
                            c2 - a2 - b2 + 2 * ab * cos(gamma) > EPS):
        if debug:
            print("not satisfying law of cosine.")
        return False

    return True


def post_check(values):
    if is_triangle(values):
        return " ".join("{:.6f}".format(v) for v in values)
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

        tri_type = "".join(map(str, data_type))

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


        elif tri_type == '010110':
            # ASA, (alpha, beta, c)
            if alpha + beta > pi:
                print("Invalid input.")
            else:
                values[5] = pi - alpha - beta
                ratio = c / sin(values[5])
                values[0] = ratio * sin(alpha)
                values[2] = ratio * sin(beta)

                # post check
                print(post_check(values))

        elif tri_type == '100101':
            # ASA (a ,beta, gamma)
            if beta + gamma > pi:
                print("Invalid input.")
            else:
                values[1] = pi - beta - gamma
                ratio = a / sin(values[1])
                values[2] = ratio * sin(beta)
                values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '011001':
            # ASA, (alpha, b, gamma)
            if alpha + gamma > pi:
                print("Invalid input.")
            else:
                values[3] = pi - alpha - gamma
                ratio = b / sin(values[3])
                values[0] = ratio * sin(alpha)
                values[4] = ratio * sin(gamma)

            # post check
            print(post_check(values))

        elif tri_type == '110100':
            # AAS  (a, alpha, beta)
            if alpha + beta > pi:
                print("Invalid input.")
            else:
                values[5] = pi - alpha - beta
                gamma = values[5]
                ratio = a / sin(alpha)
                values[2] = ratio * sin(beta)
                values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '001101':
            # AAS (b, beta, gamma)
            if gamma + beta > pi:
                print("Invalid input.")
            else:
                values[1] = pi - gamma - beta
                alpha = values[1]
                ratio = b / sin(beta)
                values[0] = ratio * sin(alpha)
                values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '010011':
            # AAS (alpha, c, gamma)
            if gamma + alpha > pi:
                print("Invalid input.")
            else:
                values[3] = pi - gamma - alpha
                beta = values[3]
                ratio = c / sin(gamma)
                values[0] = ratio * sin(alpha)
                values[2] = ratio * sin(beta)

                # post check
                print(post_check(values))

        elif tri_type == '110001':
            # AAS (a, alpha, gamma)
            if gamma + alpha > pi:
                print("Invalid input.")
            else:
                values[3] = pi - gamma - alpha
                beta = values[3]
                ratio = a / sin(alpha)
                values[2] = ratio * sin(beta)
                values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '011100':
            # AAS (alpha, b, beta)
            if alpha + beta > pi:
                print("Invalid input.")
            else:
                values[5] = pi - alpha - beta
                gamma = values[5]
                ratio = b / sin(beta)
                values[0] = ratio * sin(alpha)
                values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type == '000111':
            # AAS  (beta c, gamma)
            if gamma + beta > pi:
                print("Invalid input.")
            else:
                values[1] = pi - gamma - beta
                alpha = values[1]
                ratio = c / sin(gamma)
                values[0] = ratio * sin(alpha)
                values[2] = ratio * sin(beta)

                # post check
                print(post_check(values))


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
            # ASA (alpha, beta, c, gamma), (a, alpha, beta, gamma)
            # (alpha, b, beta, gamma)
            if not is_satisfy_angle_rule(alpha, beta, gamma):
                print("Invalid input.")
            else:
                if c > 0:
                    ratio = c / sin(gamma)
                    values[0] = ratio * sin(alpha)
                    values[2] = ratio * sin(beta)
                elif a > 0:
                    ratio = a / sin(alpha)
                    values[2] = ratio * sin(beta)
                    values[4] = ratio * sin(gamma)
                elif b > 0:
                    ratio = b / sin(beta)
                    values[0] = ratio * sin(alpha)
                    values[4] = ratio * sin(gamma)

                # post check
                print(post_check(values))

        elif tri_type in ('111100', '001111', '110011'):
            # AAS (a, alpha,b, beta), (b,beta, c gamma), (a,alpha, c, gamma)
            if gamma < 0:
                if alpha + beta > pi:
                    print("Invalid input.")
                else:
                    values[5] = pi - alpha - beta
                    gamma = values[5]
                    values[4] = a / sin(alpha) * sin(gamma)

                    # post check
                    print(post_check(values))

            elif alpha < 0:
                if beta + gamma > pi:
                    print("Invalid input.")
                else:
                    values[1] = pi - beta - gamma
                    alpha = values[1]
                    values[0] = b / sin(beta) * sin(alpha)
                    # post check
                    print(post_check(values))
            elif beta < 0:
                if alpha + gamma > pi:
                    print("Invalid input.")
                else:
                    values[3] = pi - alpha - gamma
                    beta = values[3]
                    values[2] = a / sin(alpha) * sin(beta)

                    # post check
                    print(post_check(values))


        elif tri_type in ('110110', '101101', '011011'):
            # ASA (a, alpha, beta, c), (a, b, beta, gamma), (alpha, b, c, gamma)
            if gamma < 0:
                if alpha + beta > pi:
                    print("Invalid input.")
                else:
                    values[5] = pi - alpha - beta
                    values[2] = a / sin(alpha) * sin(beta)

                    # post check
                    print(post_check(values))

            elif alpha < 0:
                if beta + gamma > pi:
                    print("Invalid input.")
                else:
                    values[1] = pi - beta - gamma
                    alpha = values[1]
                    values[4] = b / sin(beta) * sin(gamma)
                    # post check
                    print(post_check(values))

            elif beta < 0:
                if alpha + gamma > pi:
                    print("Invalid input.")
                else:
                    values[3] = pi - alpha - gamma
                    beta = values[3]
                    values[0] = b / sin(beta) * sin(alpha)

                    # post check
                    print(post_check(values))


        elif tri_type in ('011110', '100111', '111001'):
            # ASA (alpha, b, beta ,c), (a, beta, c, gamma), (a, alpha, b, gamma)
            if gamma < 0:
                if alpha + beta > pi:
                    print("Invalid input.")
                else:
                    values[5] = pi - alpha - beta
                    values[0] = b / sin(beta) * sin(alpha)

                    # post check
                    print(post_check(values))

            elif alpha < 0:
                if beta + gamma > pi:
                    print("Invalid input.")
                else:
                    values[1] = pi - beta - gamma
                    values[2] = a / sin(alpha) * sin(beta)
                    # post check
                    print(post_check(values))

            elif beta < 0:
                if alpha + gamma > pi:
                    print("Invalid input.")
                else:
                    values[3] = pi - alpha - gamma
                    values[4] = a / sin(alpha) * sin(gamma)
                    # post check
                    print(post_check(values))

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
            if not is_satisfy_angle_rule(alpha, beta, gamma):
                print("Invalid input.")
            else:
                if a < 0:
                    values[0] = b / sin(beta) * sin(alpha)
                elif b < 0:
                    values[2] = a / sin(alpha) * sin(beta)
                elif c < 0:
                    values[4] = a / sin(alpha) * sin(gamma)

                # post check
                print(post_check(values))


if __name__ == '__main__':
    main()
