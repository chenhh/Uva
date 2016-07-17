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
from math import (pi, cos, acos, sin, sqrt)

EPS = 1e-6


def is_all_positive(vals):
    for val in vals:
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


def is_triangle(vals):
    a, alpha, b, beta, c, gamma = vals
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


def post_check(vals):
    if is_triangle(vals):
        return " ".join(":.6f".format(v for v in vals))
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
        vals = list(map(float, next(recs).split()))
        a, alpha, b, beta, c, gamma = vals

        # negative values are the unknown variables
        data_type = [1] * 6
        n_known = 6
        for idx, val in enumerate(vals):
            if val <= 0:
                data_type[idx] = 0
                n_known -= 1

        if n_known <= 2:
            # all the edges or all the angles are unknown.
            print("Invalid input.")
            continue

        triangle_type = "".join(data_type)

        if triangle_type == '111111':
            # all edges and angles are known
            print(post_check(vals))

        elif triangle_type == '010101':
            # AAA, no finite solutions.
            print("Invalid input.")

        elif triangle_type == '101010':
            # SSS, only three edges are known, no multiple solution.
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                # recover
                vals[1] = law_of_cosine_to_angle(a, b, c)
                vals[3] = law_of_cosine_to_angle(b, a, c)
                vals[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(vals))

        elif triangle_type in ('101001', '011010', '100110'):
            # SAS (a,b,gamma), (alpha,b,c), (a,beta, c)
            if alpha > pi or beta > pi or gamma > pi:
                # law of angle
                print("Invalid input.")
            else:
                if alpha > 0:
                    vals[0] = law_of_cosine_to_edge(alpha, b, c)
                    vals[3] = law_of_cosine_to_angle(b, vals[0], c)
                    vals[5] = law_of_cosine_to_angle(c, vals[0], b)
                elif beta > 0:
                    vals[2] = law_of_cosine_to_edge(beta, a, c)
                    vals[1] = law_of_cosine_to_angle(a, vals[2], c)
                    vals[5] = law_of_cosine_to_angle(c, a, vals[2])
                elif gamma > 0:
                    vals[4] = law_of_cosine_to_edge(gamma, a, b)
                    vals[1] = law_of_cosine_to_angle(a, b, vals[4])
                    vals[3] = law_of_cosine_to_angle(b, a, vals[4])

                # post check
                print(post_check(vals))

        elif triangle_type in ('111000', '001110', '100011'):
            # SSA (a,alpha, b), (b,beta, c), (a,c, gamma)
            if alpha > pi or beta > pi or gamma > pi:
                # law of angle
                print("Invalid input.")
            elif ((alpha > pi / 2 and a < b) or
                      (beta > pi / 2 and b < c) or
                      (gamma > pi / 2 and c < b)):
                # law of sine.
                print("Invalid input.")
                # TODO

        elif triangle_type in ('110010', '101100', '001011'):
            # ASS (a,alpha, c), (a,b, beta), (b,c, beta)
            # TODO
            pass

        elif triangle_type in ('010110', '100101', '011001'):
            # ASA
            pass
        elif triangle_type in ('110100', '001101', '010011'):
            # AAS
            pass

        elif triangle_type('110001', '011100', '000111'):
            # SAA
            pass

        elif triangle_type in ('111010', '101110', '101011'):
            # SSS, three edges and one angle are known, no multiple solution.
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                # recover
                if alpha > 0:
                    vals[3] = law_of_cosine_to_angle(b, a, c)
                    vals[5] = law_of_cosine_to_angle(c, a, b)
                elif beta > 0:
                    vals[1] = law_of_cosine_to_angle(a, b, c)
                    vals[5] = law_of_cosine_to_angle(c, a, b)
                elif gamma > 0:
                    vals[1] = law_of_cosine_to_angle(a, b, c)
                    vals[3] = law_of_cosine_to_angle(b, a, c)

                # post check
                print(post_check(vals))

        elif triangle_type in ('010111', '110101', '011101'):
            # ASA
            pass

        elif triangle_type in ('111100', '001111', '110011'):
            # AAS
            pass
        elif triangle_type in ('110110', '101101', '011011'):
            # ASA
            pass
        elif triangle_type in ('011110', '100111', '111001'):
            # ASA
            pass

        elif triangle_type in ('111110', '101111', '111011'):
            # SSS, three edges and two angles are known
            if not is_satisfy_triangle_inequality(a, b, c):
                print("Invalid input.")
            else:
                if alpha < 0:
                    vals[1] = law_of_cosine_to_angle(a, b, c)
                elif beta < 0:
                    vals[3] = law_of_cosine_to_angle(b, a, c)
                elif gamma < 0:
                    vals[5] = law_of_cosine_to_angle(c, a, b)

                # post check
                print(post_check(vals))

        elif triangle_type in ('011111', '110111', '111101'):
            # ASA
            pass

        
if __name__ == '__main__':
    main()
